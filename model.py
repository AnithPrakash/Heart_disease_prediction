import pickle
import streamlit as st

model=(open("D:/DATA SCIENCE/PROJECTS DONE BY ME/P1/model.sav"))
model1=pickle.loads(open(model,'rb'))

st.title("Heart Disease Prediction")

col1, col2, col3 = st.columns(3)
with col1:
    age=st.text_input("Enter your Age")

with col2:
    sex=st.text_input("Enter your Sex (1 or 0)")

with col3:
    cp=st.text_input("Enter your CP ( level=1/2/3/0 )")

with col1:
    tresrbps=st.text_input("Enter your TresrBPS")

with col2:
    chol=st.text_input("Enter your chol")

with col3:
    fbs=st.text_input("enter your FBS (1 or 0)")

with col1:
    restecg=st.text_input("enter your ECG (1 or 0)")

with col2:
    thalach=st.text_input("Enter your Thalach")

with col3:
    exang=st.text_input("Enter your exang(1 or 0)")

with col1:
    oldpeak=st.text_input("Enter your oldpeak(float value)")

with col2:
    slope=st.text_input("Enter your slope ( 0 / 1 / 2)")

with col3:
    cs=st.text_input("Enter your CA (0 / 1 / 2)")

with col2:
    thal=st.text_input("Enter your Thal (0 / 1 / 2)")

heart_diagnosis=''
if st.button('Result'):
    predictive=model1.predict(
        [[age,sex,cp,tresrbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,cs,thal]])
    if predictive[0]==0:
        print("your safe you dont have hearts disease")
    else:
        print("your die mahn, you have it ")
st.success(predictive)


