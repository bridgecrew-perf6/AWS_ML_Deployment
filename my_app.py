from contextlib import redirect_stderr
from inspect import ClassFoundException
from logging import captureWarnings
from telnetlib import STATUS
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle


img = Image.open("scout.png")
st.image(img, width=600)


brand = st.sidebar.selectbox("Make Model:",["Audi A1", "Audi A3", "Opel Astra", "Opel Corsa", "Opel Insignia", "Renault Espace", "Renault Clio", "Renault Duster"])
age = st.sidebar.number_input("Age:",min_value=0, max_value=3)
gearing_type = st.sidebar.radio("Gearing Type:",["Manual", "Automatic", "Semi-automatic"])
km = st.sidebar.slider("Km:", 0,200000, step=500)
hp_kW = st.sidebar.number_input("HP:",min_value=44, max_value=294)

if brand=="Audi A1":
    st.image(Image.open("a1.jpg"),width=450)
elif brand == "Audi A3":
    st.image(Image.open("a3.jpg"),width=450)
elif brand == "Opel Astra":
    st.image(Image.open("astra.jpg"),width=450)
elif brand == "Opel Corsa":
    st.image(Image.open("corsa.jpg"),width=450)
elif brand == "Opel Insignia":
    st.image(Image.open("insignia.jpg"),width=450)
elif brand == "Renault Espace":
    st.image(Image.open("espace.jpg"),width=450)
elif brand == "Renault Clio":
    st.image(Image.open("clio.jpg"),width=450)
elif brand == "Renault Duster":
    st.image(Image.open("duster.jpg"),width=450)


model_name=st.selectbox("Select your model:",("XGBOOST","Random Forest"))

if model_name=="XGBOOST":
	model=pickle.load(open("xgb_model","rb"))
	st.success("You selected {} model".format(model_name))
else :
	model=pickle.load(open("rf_model","rb"))
	st.success("You selected {} model".format(model_name))



my_dict = {
    "age": age,
    "hp": hp_kW,
    "km": km,
    "model": brand,
    'gearing_type':gearing_type
}

df = pd.DataFrame.from_dict([my_dict])


st.header("The features of your car is below")
st.table(df)

columns= ['age','hp', 'km', 'model_A1', 'model_A2', 'model_A3', 'model_Astra', 'model_Clio', 'model_Corsa', 'model_Espace',
'model_Insignia',
'gearing_type_Automatic',
'gearing_type_Manual',
'gearing_type_Semi-automatic']


df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

st.subheader("Press Price predict if configuration is okay")

if st.button("Price Predict"):
    prediction = model.predict(df)
    st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))