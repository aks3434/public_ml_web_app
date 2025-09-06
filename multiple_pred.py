import streamlit as st
import pickle 
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open(r"C:\Users\ad859\Desktop\Multiple_diseas_pred\saved_models\trained_model.sav" , 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\ad859\Desktop\Multiple_diseas_pred\saved_models\heart_disease_model.sav" , "rb"))
breast_cancer_model = pickle.load(open(r"C:\Users\ad859\Desktop\Multiple_diseas_pred\saved_models\trained_breast_model.sav" , 'rb'))

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System" , 
                           ["Diabetes Prediction",
                            'Heart Disease Prediction' , 
                             'Breast Cancer Prediction'],
                             icons = ['activity' , 'heart' ,'person'],
                             default_index=0)


if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')

    #Getting the input data from the user 
    #columns for input field
    col1 , col2 , col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose level')

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin level')

    with col3:
         BMi = st.text_input('BMI value')


    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')

    with col2:
        Age =st.text_input('Age of the Person')

        
    #Code for prediction 
    diab_diagnosis = ''
    #creating a button for prediction 
    
    if st.button("Diabetes Test Result"):
        try:
            user_input = [
                float(Pregnancies), float(Glucose) , float(BloodPressure),
                float(SkinThickness) , float(Insulin) , float(BMi) , float(DiabetesPedigreeFunction ), float(Age)
            ]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        except ValueError:
            diab_diagnosis = "Please enter valid numeric values!"

    st.success(diab_diagnosis)

        


if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')

if (selected == 'Breast Cancer Prediction'):
    st.title("Breast Cancer Prediction using ML")

    























