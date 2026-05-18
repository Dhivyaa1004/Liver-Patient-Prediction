
""" CREATED BY: 2024-06-01
@author: Dhivyaa1004
"""

# -----------------------------------
# Import Libraries
# -----------------------------------

import streamlit as st
import pandas as pd
import pickle

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------------
# Custom CSS Styling
# -----------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: white !important;
    }

    .stButton>button {
        background-color: #22c55e;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #16a34a;
        color: white;
    }

    input {
        background-color: #1e293b !important;
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# Stylish Header
# -----------------------------------

html_temp = """
<div style="
background: linear-gradient(90deg,#0f172a,#1e293b);
padding:25px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.3);
margin-bottom:25px;
">

<h1 style="
color:white;
text-align:center;
font-size:38px;
font-family:Arial;
margin-bottom:5px;
">
🩺 Liver Disease Prediction System
</h1>

<p style="
color:#cbd5e1;
text-align:center;
font-size:18px;
">
Machine Learning Based Liver Patient Analysis
</p>

</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)

# -----------------------------------
# Load Trained Model
# -----------------------------------

try:

    with open('best_model.pkl', 'rb') as f:
        best_model = pickle.load(f)

    with open('feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)

except FileNotFoundError:

    st.error("Model files not found.")

except Exception as e:

    st.error(f"Error loading model: {e}")

# -----------------------------------
# Prediction Function
# -----------------------------------

def predict_liver_disease(input_data):

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])

    # Arrange columns properly
    input_df = input_df[feature_names]

    # Prediction
    prediction = best_model.predict(input_df)[0]

    # Prediction Probability
    probability = best_model.predict_proba(input_df)[0][1]

    # Final Output
    if prediction == 1:
        result = "⚠️ Liver Disease Detected"
    else:
        result = "✅ No Liver Disease"

    return result, probability

# -----------------------------------
# User Input Section
# -----------------------------------

st.subheader("Enter Patient Medical Details")

Age = st.text_input(
    "Age",
    placeholder="Type Here"
)

Gender = st.selectbox(
    "Gender",
    ["Select Gender", "Male", "Female"]
)

Total_Bilirubin = st.text_input(
    "Total Bilirubin",
    placeholder="Type Here"
)

Direct_Bilirubin = st.text_input(
    "Direct Bilirubin",
    placeholder="Type Here"
)

Alkaline_Phosphotase = st.text_input(
    "Alkaline Phosphotase",
    placeholder="Type Here"
)

Alamine_Aminotransferase = st.text_input(
    "Alamine Aminotransferase",
    placeholder="Type Here"
)

Aspartate_Aminotransferase = st.text_input(
    "Aspartate Aminotransferase",
    placeholder="Type Here"
)

Total_Protiens = st.text_input(
    "Total Protiens",
    placeholder="Type Here"
)

Albumin = st.text_input(
    "Albumin",
    placeholder="Type Here"
)

Albumin_and_Globulin_Ratio = st.text_input(
    "Albumin and Globulin Ratio",
    placeholder="Type Here"
)

# -----------------------------------
# Prediction Button
# -----------------------------------

if st.button("Predict Liver Disease"):

    try:

        input_data = {

            'Age': int(Age),

            'Gender': Gender,

            'Total_Bilirubin': float(Total_Bilirubin),

            'Direct_Bilirubin': float(Direct_Bilirubin),

            'Alkaline_Phosphotase': float(Alkaline_Phosphotase),

            'Alamine_Aminotransferase': float(Alamine_Aminotransferase),

            'Aspartate_Aminotransferase': float(Aspartate_Aminotransferase),

            'Total_Protiens': float(Total_Protiens),

            'Albumin': float(Albumin),

            'Albumin_and_Globulin_Ratio': float(Albumin_and_Globulin_Ratio)
        }

        result, probability = predict_liver_disease(input_data)

        # -----------------------------------
        # Stylish Result Box
        # -----------------------------------

        result_html = f"""
        <div style="
        background-color:#111827;
        padding:20px;
        border-radius:12px;
        border-left:8px solid #22c55e;
        margin-top:20px;
        ">

        <h2 style="color:white;">
        Prediction Result
        </h2>

        <p style="
        color:#22c55e;
        font-size:24px;
        font-weight:bold;
        ">
        {result}
        </p>

        <p style="
        color:#cbd5e1;
        font-size:18px;
        ">
        Prediction Probability: {probability:.2f}
        </p>

        </div>
        """

        st.markdown(result_html, unsafe_allow_html=True)

    except ValueError:

        st.error("Please enter valid numeric values.")

# -----------------------------------
# Footer
# -----------------------------------

footer_html = """
<hr>

<div style="
text-align:center;
padding:10px;
color:gray;
font-size:15px;
">

Developed with ❤️ using Streamlit & Machine Learning

</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)

