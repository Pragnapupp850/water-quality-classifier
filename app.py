import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("💧 Water Quality Risk Classifier")
st.write("Enter water sample measurements to predict potability risk.")

ph = st.number_input("pH", 0.0, 14.0, 7.0)
hardness = st.number_input("Hardness", 0.0, 500.0, 150.0)
solids = st.number_input("Solids", 0.0, 60000.0, 20000.0)
chloramines = st.number_input("Chloramines", 0.0, 15.0, 5.0)
sulfate = st.number_input("Sulfate", 0.0, 500.0, 250.0)
conductivity = st.number_input("Conductivity", 0.0, 1000.0, 400.0)
organic_carbon = st.number_input("Organic Carbon", 0.0, 30.0, 10.0)
trihalomethanes = st.number_input("Trihalomethanes", 0.0, 130.0, 60.0)
turbidity = st.number_input("Turbidity", 0.0, 10.0, 4.0)

if st.button("Predict"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                             conductivity, organic_carbon, trihalomethanes, turbidity]])
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if pred == 1:
        st.success(f"✅ Likely Potable — confidence {prob:.2%}")
    else:
        st.error(f"⚠️ Likely Not Potable — confidence {(1-prob):.2%}")