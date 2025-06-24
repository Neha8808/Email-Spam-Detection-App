import streamlit as st
import joblib

# ✅ Set page config FIRST
st.set_page_config(page_title="Email Spam Detector", layout="centered")

# ✅ Then hide cloud elements
hide_streamlit_cloud_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    a[title="View source"] {display: none !important;}
    button[kind="icon"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_cloud_elements, unsafe_allow_html=True)

# ✅ Load the saved model pipeline
model = joblib.load('spam_classifier.pkl')

# ✅ UI
st.title("Email Spam Detection App")
st.write("Enter an email message below:")

email_input = st.text_area("✉️ Email Text", height=200)

if st.button("Predict"):
    if email_input.strip():
        prediction = model.predict([email_input])[0]
        result = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: **{result}**")
    else:
        st.warning("Please enter some email text.")
