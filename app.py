from flask import Flask, request, jsonify
import pickle
import re

app = Flask(__name__)

# Load model and vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# Basic cleaning function: lowercase, remove punctuation, alphanumerics only
def transform_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove punctuation
    words = text.split()
    return " ".join(words)

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Use POST or GET /predict with 'message' in JSON, form-data, or query param."})

# Prediction route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    message = None

    # Handle GET with query parameter
    if request.method == 'GET':
        message = request.args.get('message')

    # Handle POST requests
    elif request.method == 'POST':
        content_type = request.content_type or ''
        if 'application/json' in content_type:
            data = request.get_json(silent=True)
            if data:
                message = data.get('message')
        elif 'multipart/form-data' in content_type or 'application/x-www-form-urlencoded' in content_type:
            message = request.form.get('message')

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    # Process and predict
    transformed_sms = transform_text(message)
    vector_input = vectorizer.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    prediction = "Spam" if result == 1 else "Not Spam"
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
