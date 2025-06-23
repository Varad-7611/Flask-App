# 📦 Spam Detection Flask API

This project is a lightweight **Flask-based REST API** that serves a machine learning model trained to classify text messages as **Spam** or **Not Spam**. The model uses **TF-IDF vectorization** and is built with **Scikit-learn**.

The API is designed to be easily integrated into any frontend — in this case, it's connected to an **Android app** built using Java and Volley.

---

## 🔧 Tech Stack

- 🧠 **Scikit-learn** – for model training (Logistic Regression)
- 📊 **TF-IDF Vectorizer** – for text transformation
- 🧪 **Flask** – for building the REST API
- ☁️ **Render** – for hosting the API


---

## ⚙️ How It Works

1. User sends a message to the API endpoint (`/predict`) via a GET or POST request.
2. The API:
   - Preprocesses the text (lowercase, remove punctuation, split, etc.)
   - Vectorizes the input using the saved `TfidfVectorizer`
   - Uses the trained ML model to predict the label
3. The API returns a JSON response:  
   ```json
   { "prediction": "Spam" }
   { "prediction": "Not Spam" }

