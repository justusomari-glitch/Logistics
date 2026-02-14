import streamlit as st
import requests
st.sidebar.title("LOGISTICS ANALYSIS")
prediction_type=st.sidebar.selectbox("Select Prediction Type:",["Revenue Prediction","Customer Segmentation","Inspection Prediction","Shipping Costs Prediction"])

if prediction_type=="Customer Segmentation":
    st.header("CUSTOMER SEGMENTATION")
elif prediction_type=="Inspection Prediction":
        st.header("INSPECTION PREDICTION")
elif prediction_type=="Revenue Prediction":
        st.header("REVENUE PREDICTION")
elif prediction_type=="Shipping Costs Prediction":
        st.header("SHIPPING COSTS PREDICTION")

Customer_demographics=['Female','Male','Non-binary','Unknown']

Product_type=['cosmetics','haircare','skincare']

form_values2={
    'Customer demographics':None,
    'Product type':None,
    'Price':None,
    'Number of products sold':None,
    'Revenue generated':None,
    "Availability":None
}

if prediction_type=="Customer Segmentation":
   
   Customer_demographics=['Female','Male','Non-binary','Unknown']
   Product_type=['cosmetics','haircare','skincare']
   form_values2={
        'Customer demographics':None,
        'Product type':None,
        'Price':None,
        'Number of products sold':None,
        'Revenue generated':None,
        "Availability":None
   }

   with st.form(key="customer_form"):
        form_values2['Customer demographics']=st.selectbox("Select Customer Demographics:", Customer_demographics)
        form_values2['Product type']=st.selectbox("Select Product Type:", Product_type)
        form_values2['Price']=st.number_input("Enter Price:",min_value=5.0)
        form_values2['Number of products sold']=st.number_input("Enter Number of Products Sold:",min_value=10)
        form_values2['Revenue generated']=st.number_input("Enter Revenue Generated:")
        form_values2["Availability"]=st.number_input("Enter Availability:",min_value=3)
        submit_button=st.form_submit_button(label="Customer Segmentation:")
        if submit_button:
            input_data={
                'Customer_demographics': form_values2['Customer demographics'],
                'Product_type': form_values2['Product type'],
                'Price': form_values2['Price'],
                'Number_of_products_sold': form_values2['Number of products sold'],
                'Revenue_generated': form_values2['Revenue generated'],
                'Availability': form_values2["Availability"] 
            }
            url="https://logistics-2-ever.onrender.com/predict/customer_segmentation"
            response=requests.post(url,json=input_data)
            st.write(response.json())
elif prediction_type=="Revenue Prediction":
      Customer_demographics=['Female','Male','Non-binary','Unknown']
      Product_type=['cosmetics','haircare','skincare']
      customer_classification=['Mid-tier customers','Highest-value customers','High-value customers','Low-value customers']
      form_values3={
        'Customer demographics':None,
        'Product type':None,
        'Price':None,
        'Number of products sold':None,
        "Availability":None,
        'customer_classification':None
      }

      with st.form(key="revenue_form"):
           form_values3['Customer demographics']=st.selectbox("Select Customer Demographics:", Customer_demographics)
           form_values3['Product type']=st.selectbox("Select Product Type:", Product_type)
           form_values3['Price']=st.number_input("Enter Price:",min_value=5.0)
           form_values3['Number of products sold']=st.number_input("Enter Number of Products Sold:",min_value=10)
           form_values3["Availability"]=st.number_input("Enter Availability:",min_value=3)
           form_values3['customer_classification']=st.selectbox("Select Customer Classification:", customer_classification)
           submit_button=st.form_submit_button(label="Revenue Prediction:")

           if submit_button:
                input_data={
                    'Customer_demographics': form_values3['Customer demographics'],
                    'Product_type': form_values3['Product type'],
                    'Price': form_values3['Price'],
                    'Number_of_products_sold': form_values3['Number of products sold'],
                    'Availability': form_values3["Availability"],
                    'customer_classification': form_values3['customer_classification']
                }
                url="https://logistics-2-ever.onrender.com/predict/revenue"
                response=requests.post(url,json=input_data)
                st.write(response.json())
           


     
      
                 
