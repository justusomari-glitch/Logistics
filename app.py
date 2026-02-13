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

@app.post("predict")
def predict(data: LogisticsData):
    input_dict= data.model_dump()
    mapped_dict={
        'Supplier_name': input_dict['Supplier_name'],
        'Defect_rates': input_dict['Defect_rates'],
        'Production_volumes': input_dict['Production_volumes'],
        'Manufacturing_lead_time': input_dict['Manufacturing_lead_time'],
        'Manufacturing_costs': input_dict['Manufacturing_costs'],
        'Price': input_dict['Price'],
        'Availability': input_dict['Availability'],
        'Number_of_products_sold': input_dict['Number_of_products_sold'],
        'Revenue_generated': input_dict['Revenue_generated'],
        'Product_type': input_dict['Product_type'],
        'Customer_demographics': input_dict['Customer_demographics'],
        'customer_classification': input_dict['customer_classification'],
        'Transportation_modes': input_dict['Transportation_modes'],
        'Routes': input_dict['Routes'],
        'Shipping_carriers': input_dict['Shipping_carriers'],
        'Shipping_times': input_dict['Shipping_times'],
        'Order_quantities': input_dict['Order_quantities']
    }
    input_df=pd.DataFrame([mapped_dict])

    inspection_df=input_df[inspection_model.feature_names_in_]
    customer_df=input_df[customer_model.feature_names_in_]
    revenue_df=input_df[revenue_model.feature_names_in_]
    shipping_df=input_df[shipping_model.feature_names_in_]
    
    inspection_prediction=inspection_model.predict(inspection_df)
    customer_prediction=customer_model.predict(customer_df)
    revenue_prediction=revenue_model.predict(revenue_df)
    shipping_prediction=shipping_model.predict(shipping_df)
    return {
        "inspection_prediction": inspection_prediction[0],
        "customer_prediction": customer_prediction[0],
        "revenue_prediction": revenue_prediction[0],
        "shipping_prediction": shipping_prediction[0]
    }
