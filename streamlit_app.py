import streamlit as st
import requests


st.title("LOGISTICS ANALYSIS")
st.header("CUSTOMER SEGMENTATION")

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
    if None in form_values2.values():
        st.warning("Please fill in all the fields.")
    else:input_data={
        'Customer demographics': form_values2['Customer demographics'],
        'Product type': form_values2['Product type'],
        'Price': form_values2['Price'],
        'Number of products sold': form_values2['Number of products sold'],
        'Revenue generated': form_values2['Revenue generated'],
        "Availability": form_values2["Availability"]
    }
url="https://logistics-2-ever.onrender.com/predict/customer_segmentation"

response=requests.post(url,json=input_data)
st.write(response)
