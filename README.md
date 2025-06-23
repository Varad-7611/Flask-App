# Spam Detection API

This is a Flask-based spam detection API using a machine learning model.

## 🚀 How to Deploy on [Render](https://render.com)

1. Push this project to GitHub
2. Go to [https://render.com](https://render.com) > New Web Service
3. Connect your repo
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Python version: 3.9+

## API Endpoint

- **GET** `/predict?message=your_message`
  - Response: `{ "prediction": "Spam" }` or `{ "prediction": "Not Spam" }`
