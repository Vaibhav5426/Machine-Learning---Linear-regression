import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")
st.title("💼 Salary Prediction App")

@st.cache_resource
def load_model():
    with open("linear_regression.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
    years_experience = st.number_input("Years of Experience", min_value=0.0, max_value=40.0, value=1.0, step=0.5)

    if st.button("Calculate Predicted Salary", type="primary"):
        features = np.array([[years_experience]])
        prediction = model.predict(features)
        st.subheader(f"Estimated Salary: ${prediction[0]:,.2f}")
except FileNotFoundError:
    st.error("Error: 'linear_regression.pkl' not found. Make sure the model file is committed in your repository.")
