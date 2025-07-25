import streamlit as st
import pickle

# Load model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("📰 Fake News Detector")

input_text = st.text_area("Enter News Text Below:")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        transformed_text = vectorizer.transform([input_text])
        prediction = model.predict(transformed_text)
        if prediction[0] == "REAL":
            st.success("✅ Prediction: REAL NEWS")
        else:
            st.error("🚨 Prediction: FAKE NEWS")
