# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 08:01:52 2023

@author: navanit
"""

#importing required libraries
import pickle
import streamlit as st
import numpy as np

#setting page title
st.set_page_config(page_title = "ABC Multinational Bank", page_icon = ":bank:")

#loading the saved model
loaded_model = pickle.load(open('final_model.sav', 'rb'))
    
#creating a function for prediction
def predict(input_data):
    #changing input_data to numpy array
    input_np = np.array(input_data)
    #reshaping the array
    input_np_rs = input_np.reshape(1,-1)
    prediction = loaded_model.predict(input_np_rs)
    if(prediction[0] == 0):
        #Non churner
        ret_str = "Customer is likely to stay"
    else:
        #churner
        ret_str = "Customer is likely to leave" 
    return ret_str
        
def main():
    #title
    st.title(":bank: ABC Multinational Bank")
    st.header("Customer churn predictor")
    #getting input from user
    credit_score = st.number_input("Credit score", min_value=300, max_value=850)
    temp = st.selectbox("Country",("France","Germany","Spain"))
    if(temp == "France"):
        country = 0
    elif(temp == "Germany"):
        country = 1
    else:
        country = 2
    temp = st.selectbox("Gender",("Male","Female"))
    if(temp == "Male"):
        gender = 1
    else:
        gender = 0
    age	= st.number_input("Age", min_value=18)
    tenure = st.number_input("Tenure")
    balance = st.number_input("Balance")
    products_number	 = st.number_input("Number of products", min_value=1)
    temp = st.radio("Does the customer have a credit card from the bank?",
                           ("Yes", "No"))
    if(temp == "Yes"):
        credit_card = 1
    else:
        credit_card = 0
    temp = st.radio("Is the customer an active member?",
                           ("Yes", "No"))
    if(temp == "Yes"):
        active_member = 1
    else:
        active_member = 0	
    estimated_salary = st.number_input("Estimated salary")
    
    result = ''
    #creating a button for prediction
    if st.button('Predict'):
        result = predict([credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary])
    #printing the result
    st.success(result)
    
if __name__ == '__main__':
    main()