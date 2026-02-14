import streamlit as st
import requests
st.sidebar.title("LOGISTICS ANALYSIS")
st.sidebar.markdown("Welcome to the Logistics Analysis App! This application provides insights and predictions related to various aspects of logistics, including revenue prediction, customer segmentation, inspection prediction, and shipping costs prediction. Please select a prediction type to get started.")   
prediction_type=st.sidebar.selectbox("Select Prediction Type:",["Revenue Prediction","Customer Segmentation","Inspection Prediction","Shipping Costs Prediction"])
st.markdown("## Please fill in the required information to get the prediction results.")
st.sidebar.caption("Built By Omari Kwache Justus Junior")
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
            url="https://logistics-1vg4.onrender.com/predict/customer_segmentation"
            response=requests.post(url,json=input_data)
            customer_segmentation=response.json()
            prediction=customer_segmentation.get("customer_segmentation")
            st.write(f"### Customer Group: {prediction}")


elif prediction_type=="Revenue Prediction":
      Customer_demographics=['Female','Male','Non-binary','Unknown']
      Product_type=['cosmetics','haircare','skincare']
      customer_classification=['Mid-tier Customer','Highest Value Customer','High Value Customer','Low Value Customer']
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
                url="https://logistics-1vg4.onrender.com/predict/revenue"
                response=requests.post(url,json=input_data)
                Revenue=response.json()
                prediction=Revenue.get("revenue_prediction")
                st.write(f"#### Predicted Revenue: {prediction}")


elif prediction_type=="Inspection Prediction":
      Supplier_name=['Supplier 1','Supplier 2','Supplier 3','Supplier 4','Supplier 5']
      form_values4={
            "Supplier name":None,
            "Defect rates":None,
            "Production volumes":None,
            "Manufacturing lead time":None,
            "Manufacturing costs":None
      }
      with st.form(key="inspection_form"):
            form_values4["Supplier name"]=st.selectbox("Select Supplier Name:", Supplier_name)
            form_values4["Defect rates"]=st.number_input("Enter Defect Rates:",min_value=2.0)
            form_values4["Production volumes"]=st.number_input("Please enter production Volumes:",min_value=1)
            form_values4["Manufacturing lead time"]=st.number_input("Please enter Manufacturing Lead Time:",min_value=1)
            form_values4["Manufacturing costs"]=st.number_input("Please enter Manufacturing Costs:",min_value=1)
            submit_button=st.form_submit_button(label="inspection Prediction")
            if submit_button:
                input_data={ 
                    "Supplier_name": form_values4["Supplier name"],
                    "Defect_rates": form_values4["Defect rates"],
                    "Production_volumes": form_values4["Production volumes"],
                    "Manufacturing_lead_time": form_values4["Manufacturing lead time"],
                    "Manufacturing_costs": form_values4["Manufacturing costs"]
                }
                url="https://logistics-1vg4.onrender.com/predict/inspection"
                response=requests.post(url,json=input_data)
                inspection_prediction=response.json()
                prediction=inspection_prediction.get("inspection_prediction")
                st.write(f"### Inspection Outcome: {prediction}")


elif prediction_type=="Shipping Costs Prediction":
      Transportation_mode=['Air','Sea','Rail','Road']
      Routes=['Route A','Route B','Route C']
      Shipping_carriers=['Carrier A','Carrier B','Carrier C']

      form_values5={
            "Transportation modes":None,
            "Routes":None,
            "Shipping carriers":None,
            "Shipping times":None,
            "Order quantities":None
      }
       
      with st.form(key="shipping_costs_form"):
           form_values5['Transportation modes']=st.selectbox('Pick Transporttion Mode:',Transportation_mode)
           form_values5['Routes']=st.selectbox("Pick Routes:",Routes)
           form_values5['Shipping carriers']=st.selectbox("Pick Shipping Carriers:",Shipping_carriers)
           form_values5['Shipping times']=st.number_input("Enter Shipping Times:",min_value=1)
           form_values5['Order quantities']=st.number_input("Enter Order Quantities:",min_value=1)
           submit_button=st.form_submit_button(label="Shipping Costs Prediction")
           if submit_button:
                input_data={
                    "Transportation_modes": form_values5["Transportation modes"],
                    "Routes": form_values5["Routes"],
                    "Shipping_carriers": form_values5["Shipping carriers"],
                    "Shipping_times": form_values5["Shipping times"],
                    "Order_quantities": form_values5["Order quantities"]
                }
                url="https://logistics-1vg4.onrender.com/predict/shipping costs"
                response=requests.post(url,json=input_data)
                Shipping_costs=response.json()
                prediction=Shipping_costs.get("shipping_costs_prediction")
                st.write(f"### Shipping Costs: {prediction}")