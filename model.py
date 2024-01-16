import pickle
import streamlit as st

model="model.sav"
model1=pickle.load(open(model,'rb'))

st.title("Heart Disease Prediction")

col1, col2, col3 = st.columns(3)
with col1:
    age=st.text_input("Enter your Age")

with col2:
    sex=st.text_input("Enter your Sex (1 or 0)")

with col3:
    cp=st.text_input("Enter your Chest Pain types")

with col1:
    tresrbps=st.text_input("Enter your Resting Blood Pressure")

with col2:
    chol=st.text_input("Enter your Serum Cholestoral ")

with col3:
    fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")

with col1:
    restecg=st.text_input("enter your ECG")

with col2:
    thalach=st.text_input("Enter your Maximum Heart Rate ")

with col3:
    exang=st.text_input("Enter your Exercise Induced Angina")

with col1:
    oldpeak=st.text_input("ST depression induced by \n exercise")

with col2:
    slope=st.text_input("Enter your Slope of the peak exercise \n ( 0 / 1 / 2)")

with col3:
    cs=st.text_input("Enter your Major vessels colored by flourosopy (0 / 1 / 2)")

with col2:
    thal=st.text_input("Enter your Thal ( 0 = normal \n 1 = fixed defect | 2 = reversable defect)")

heart_diagnosis=''
if st.button('Result'):
    predictive=model1.predict(
        [[age,sex,cp,tresrbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,cs,thal]])
    if predictive[0]==0:
        heart_diagnosis="your safe you dont have hearts disease"
    else:
        heart_diagnosis="your done mahn, you have it "
st.success(heart_diagnosis)


