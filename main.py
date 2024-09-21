import streamlit as st
from model import FeedbackSentimentAnalyzer

# ------- MODELS INIT ------- #
model = FeedbackSentimentAnalyzer()

# ------- STREAMLIT APP ------- #

# Set up the page layout and title
st.set_page_config(page_title="😍😑😩 Feedback Sentiment Analyzer", layout="centered")
st.title("Feedback Sentiment Analyzer")

# Description and instructions
st.write("""
Welcome! I'm using two advanced pre-trained models to analyze the sentiment and emotions in text inputs such as **comments, reviews, feedback, and more**.
These insights are valuable for understanding customer feelings, assessing service quality, and identifying unmet needs.
""")

# Models description
st.subheader("Models description")
st.markdown("""
- **Sentiment Analysis**: A [RoBERTa-based model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) trained on Twitter data that determines if a message is **positive, negative, or neutral**.
- **Emotion Detection**: A [DistilRoBERTa model](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) that identifies the underlying emotions in the text, such as **joy, sadness, anger, and others**.
""")

# Text input for the message
message = st.text_area("Try it out! Type some message below, and I'll provide a simple breakdown of both the sentiment and the emotion it conveys.")

# Analyze button
if st.button("Analyze Sentiment"):
    if not message.strip():
        st.error("Please enter a message.")
    else:
        # Run the sentiment and emotion analysis
        sentiment = model.sentiment_pipeline(message)
        emotion = model.emotion_pipeline(message)

        # Display the results
        sentiment_score = sentiment[0]['score'] * 100
        sentiment_label = sentiment[0]['label'].replace('LABEL_', '')
        emotion_score = emotion[0]['score'] * 100
        emotion_label = emotion[0]['label']

        # Display sentiment and emotion results
        st.markdown(f"**Sentiment Prediction:** This message has a **{sentiment_label}** sentiment with **{sentiment_score:.2f}%** confidence.")
        st.progress(sentiment_score / 100)

        st.markdown(f"**Emotion Prediction:** The emotion is **{emotion_label}** with a confidence of **{emotion_score:.2f}%**.")
        st.progress(emotion_score / 100)




