import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
inspection_model=joblib.load('inspections.pkl')
customer_model=joblib.load('kmeansclusters.pkl')
revenue_model=joblib.load('revenue_prediction.pkl')
shipping_model=joblib.load('shipping_costs.pkl')

print("inspection:",inspection_model.feature_names_in_)
print("customer:",customer_model.feature_names_in_)
print("revenue:",revenue_model.feature_names_in_)
print("shipping:",shipping_model.feature_names_in_)

@app.get("/")
def home():
    return {"message": "We are live!"}

class LogisticsData(BaseModel):
    Supplier_name: str
    Defect_rates: float
    Production_volumes: int
    Manufacturing_lead_time: int
    Manufacturing_costs: float
    Price: float
    Availability: int
    Number_of_products_sold: int
    Revenue_generated: float
    Product_type: str
    Customer_demographics: str
    customer_classification: str
    Transportation_modes: str
    Routes: str
    Shipping_carriers: str
    Shipping_times: int
    Order_quantities: int

def map_input(input_dict):
    return {
        'Supplier_name': input_dict['Supplier name'],
        'Defect_rates': input_dict['Defect rates'],
        'Production_volumes': input_dict['Production volumes'],
        'Manufacturing_lead_time': input_dict['Manufacturing lead time'],
        'Manufacturing_costs': input_dict['Manufacturing costs'],
        'Price': input_dict['Price'],
        'Availability': input_dict['Availability'],
        'Number_of_products_sold': input_dict['Number of products sold'],
        'Revenue_generated': input_dict['Revenue generated'],
        'Product_type': input_dict['Product type'],
        'Customer_demographics': input_dict['Customer demographics'],
        'customer_classification': input_dict['customer classification'],
        'Transportation_modes': input_dict['Transportation modes'],
        'Routes': input_dict['Routes'],
        'Shipping_carriers': input_dict['Shipping carriers'],
        'Shipping_times': input_dict['Shipping times'],
        'Order_quantities': input_dict['Order quantities']
    }

@app.post("/predict/customer segmentation")
def predict_customer_segmentation(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    customer_df=input_df[customer_model.feature_names_in_]
    prediction=customer_model.predict(customer_df)
    return {"customer_segmentation": prediction[0]}
   
    
@app.post("/predict/inspection")
def predict_inspection(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    inspection_df=input_df[inspection_model.feature_names_in_]
    prediction=inspection_model.predict(inspection_df)
    return {"inspection_prediction": prediction[0]}

@app.post("/predict/revenue")
def predict_revenue(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    revenue_df=input_df[revenue_model.feature_names_in_]
    prediction=revenue_model.predict(revenue_df)
    return {"revenue_prediction": prediction[0]}


@app.post("/predict/shipping costs")
def predict_shipping_costs(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    shipping_df=input_df[shipping_model.feature_names_in_]
    prediction=shipping_model.predict(shipping_df)
    return {"shipping_costs_prediction": prediction[0]}

