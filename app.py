{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46ee7a07-66a5-4f9e-9d9e-aaa4b0ec1f3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Configure the web page\n",
    "st.set_page_config(page_title=\"Salary Predictor\", page_icon=\"💼\", layout=\"centered\")\n",
    "\n",
    "st.title(\"💼 Salary Prediction App\")\n",
    "st.write(\"Enter your years of experience below to estimate your salary based on the trained regression model.\")\n",
    "\n",
    "# Load the model with caching to prevent reloading on every interaction\n",
    "@st.cache_resource\n",
    "def load_model():\n",
    "    with open(\"linear_regression.pkl\", \"rb\") as file:\n",
    "        return pickle.load(file)\n",
    "\n",
    "try:\n",
    "    model = load_model()\n",
    "\n",
    "    # Input field for user\n",
    "    years_experience = st.number_input(\n",
    "        \"Years of Experience\", \n",
    "        min_value=0.0, \n",
    "        max_value=40.0, \n",
    "        value=1.0, \n",
    "        step=0.5\n",
    "    )\n",
    "\n",
    "    # Predict button\n",
    "    if st.button(\"Calculate Predicted Salary\", type=\"primary\"):\n",
    "        # Format input for scikit-learn (2D array)\n",
    "        features = np.array([[years_experience]])\n",
    "        prediction = model.predict(features)\n",
    "        \n",
    "        # Display the result\n",
    "        st.subheader(f\"Estimated Salary: ${prediction[0]:,.2f}\")\n",
    "\n",
    "except FileNotFoundError:\n",
    "    st.error(\"Error: 'linear_regression.pkl' not found. Make sure the model file is in the same folder as this script.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
