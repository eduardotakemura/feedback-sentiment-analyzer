# Feedback Sentiment Analyzer
This project is a sentiment and emotion analysis tool built using pre-trained transformer models. 
It allows users to input text such as feedback, reviews, and comments, and provides real-time insights into the sentiment (positive, neutral, or negative) 
and the underlying emotion (joy, sadness, anger, etc.). The project uses a **Streamlit** interface for user interaction.

## Table of Contents
1. [Overview](#overview)
2. [Demo](#demo)
3. [Installation](#installation)
4. [Models Overview ](#models-overview)
5. [Usage](#usage)
6. [Libraries](#libraries)

## Overview
The Feedback Sentiment Analyzer is a simple yet powerful tool that leverages two pre-trained transformer models to analyze both sentiment and emotion in text data.
It can be used to process customer reviews, service feedback, and more, providing valuable insights for businesses and individuals.

## Demo
You can checkout the model demo [here](https://feedback-sentiment-analyzer.streamlit.app/).

## Installation
Instructions on how to install the project locally.

```bash
# Clone this repository
$ git clone https://github.com/eduardotakemura/feedback-sentiment-analyzer.git

# Go into the repository
$ cd feedback-sentiment-analyzer

# Install dependencies
$ pip install -r requirements.txt

# Run Streamlit Frontend
$ streamlit run main.py
```

## Models Overview
The project uses two advanced models for sentiment and emotion analysis:
- **Sentiment Analysis**: Based on the [**RoBERTa**](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) model, this model is trained on Twitter data and predicts whether a message is positive, negative, or neutral.
- **Emotion Detection**: A [**DistilRoBERTa**](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) model that classifies text into different emotions such as joy, sadness, anger, and more.

## Usage
After starting the application, you can input a text message, and the model will analyze the sentiment and emotion. The analysis results will show:
- **Sentiment**: Whether the text is positive, neutral, or negative, along with a confidence score.
- **Emotion**: The primary emotion detected in the text, with a confidence score.

## Libraries
- **Transformers**: Used for loading and running the pre-trained models.
- **Streamlit**: Provides the user interface for real-time interaction with the model.

