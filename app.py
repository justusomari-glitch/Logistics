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
        'Supplier name': input_dict['Supplier_name'],
        'Defect rates': input_dict['Defect_rates'],
        'Production volumes': input_dict['Production_volumes'],
        'Manufacturing lead time': input_dict['Manufacturing_lead_time'],
        'Manufacturing costs': input_dict['Manufacturing_costs'],
        'Price': input_dict['Price'],
        'Availability': input_dict['Availability'],
        'Number of products sold': input_dict['Number_of_products_sold'],
        'Revenue generated': input_dict['Revenue_generated'],
        'Product type': input_dict['Product_type'],
        'Customer demographics': input_dict['Customer_demographics'],
        'customer classification': input_dict['customer_classification'],
        'Transportation modes': input_dict['Transportation_modes'],
        'Routes': input_dict['Routes'],
        'Shipping carriers': input_dict['Shipping_carriers'],
        'Shipping times': input_dict['Shipping_times'],
        'Order quantities': input_dict['Order_quantities']
    }
cluster_names={
    0: 'Mid-tier customers',
    1: 'Highest-value customers',
    2: 'High-value customers',
    3: 'Low-value customers'
}


@app.post("/predict/customer_segmentation")
def predict_customer_segmentation(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    customer_df=input_df[customer_model.feature_names_in_]
    prediction=customer_model.predict(customer_df)
    cluster_number=int(prediction[0])
    return {"customer_segmentation": cluster_names[cluster_number]}
   
    
@app.post("/predict/inspection")
def predict_inspection(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    inspection_df=input_df[inspection_model.feature_names_in_]
    prediction=inspection_model.predict(inspection_df)
    return {"inspection_prediction": str(prediction[0])}

@app.post("/predict/revenue")
def predict_revenue(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    revenue_df=input_df[revenue_model.feature_names_in_]
    prediction=revenue_model.predict(revenue_df)
    return {"revenue_prediction": float(prediction[0])}


@app.post("/predict/shipping costs")
def predict_shipping_costs(data: LogisticsData):
    input_dict=data.model_dump()
    mapped_input=map_input(input_dict)

    input_df=pd.DataFrame([mapped_input])
    shipping_df=input_df[shipping_model.feature_names_in_]
    prediction=shipping_model.predict(shipping_df)
    return {"shipping_costs_prediction": float(prediction[0])}

