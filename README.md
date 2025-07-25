# 📰 Fake News Detection Web App

A simple yet powerful machine learning-based web application that predicts whether a news article is **Real** or **Fake**, built using **Python**, **Scikit-learn**, and **Streamlit**.

---

## 📌 Project Overview

The Fake News Detection App is designed to classify news articles using Natural Language Processing (NLP) techniques. It uses a trained machine learning model and a TF-IDF vectorizer to predict whether an input article is fake or real based on textual patterns.

---

## ⚙️ How It Works

1. **Dataset**:
   - We used two files: `Fake.csv` and `True.csv`, containing labeled news articles.
   - Data is cleaned and merged for model training.

2. **Preprocessing & Vectorization**:
   - Text data is cleaned (lowercase, punctuation removal, stop word removal).
   - TF-IDF Vectorizer is used to convert text into numerical features.

3. **Model Training**:
   - A **Logistic Regression** model is trained on the preprocessed data.
   - The model is serialized into `model.pkl`.
   - The TF-IDF vectorizer is saved as `vectorizer.pkl`.

4. **Web App**:
   - Built with **Streamlit**.
   - Accepts news article input from the user.
   - Uses the trained model to predict whether the news is fake or real.

---

## 🧠 Algorithm Used

- **Logistic Regression**: A robust and interpretable algorithm suited for binary classification tasks like fake news detection.

---

## 📉 Limitations

⚠️ **Important Note**:
- The model is trained on a **limited dataset** (`Fake.csv` and `True.csv`) which may lead to high accuracy on known data but limited generalization on unseen or real-time data.
- The model does not perform fact-checking or validate sources. It only classifies based on learned text patterns.

---

## 🔮 Future Scope

This project can be enhanced further with:
- 🔄 **Real-Time News Integration** using news APIs.
- 📈 **Larger & diverse datasets** for better generalization.
- 🤖 **Deep Learning Models** (like BERT, LSTM) for improved accuracy.
- 🧠 **Explainable AI** using LIME/SHAP to interpret predictions.
- 👥 **User Feedback Loop** for improving model performance over time.

---

## 📁 Files Included

| File             | Description                                          |
|------------------|------------------------------------------------------|
| `app.py`         | Main Streamlit web app file                          |
| `model.pkl`      | Trained Logistic Regression model                    |
| `vectorizer.pkl` | TF-IDF vectorizer used to preprocess input text      |
| `README.md`      | Project overview and documentation                   |

---


