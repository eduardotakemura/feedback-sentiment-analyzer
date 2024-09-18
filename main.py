from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# ------- APP INIT ------- #
app = Flask(__name__)

# ------- MODELS INIT ------- #
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

# ------- ROUTES ------- #
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def analyze():
    data = request.get_json()

    if 'message' not in data:
        return jsonify({'error': 'No image provided'}), 400

    sentiment = sentiment_pipeline(data['message'])
    emotion = emotion_pipeline(data['message'])

    return jsonify({'sentiment':sentiment,'emotion':emotion})

if __name__ == '__main__':
    app.run(debug=True)
