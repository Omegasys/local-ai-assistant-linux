# intent_recognition.py
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import logging

class IntentRecognition:
    def __init__(self):
        """Initialize the intent recognizer with a simple model."""
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()

        # Sample data for training
        self.train_data = [
            ("open file", "file_action"),
            ("close file", "file_action"),
            ("set reminder", "calendar_action"),
            ("view calendar", "calendar_action"),
            ("shutdown system", "system_action"),
            ("restart system", "system_action")
        ]

        self.train()

    def train(self):
        """Train the classifier on predefined intents."""
        logging.info("Training intent recognition model...")
        texts, labels = zip(*self.train_data)
        X = self.vectorizer.fit_transform(texts)
        y = labels
        self.classifier.fit(X, y)
        logging.info("Model trained successfully.")

    def predict_intent(self, text):
        """Predict the intent of a given text."""
        text_vectorized = self.vectorizer.transform([text])
        intent = self.classifier.predict(text_vectorized)
        logging.info(f"Predicted intent: {intent[0]}")
        return intent[0]
