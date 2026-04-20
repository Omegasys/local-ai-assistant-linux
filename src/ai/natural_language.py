# natural_language.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import logging

class NaturalLanguageProcessor:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        """Preprocess the input text by tokenizing and removing stopwords."""
        tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
        filtered_tokens = [word for word in tokens if word not in self.stop_words]
        logging.info(f"Preprocessed text: {' '.join(filtered_tokens)}")
        return filtered_tokens

    def extract_entities(self, text):
        """Extract entities (e.g., dates, times, etc.) from text using simple rules."""
        # For simplicity, this method could be extended with an NER (Named Entity Recognition) model.
        tokens = self.preprocess_text(text)
        entities = [token for token in tokens if token.isalnum()]  # Basic entity extraction
        logging.info(f"Extracted entities: {entities}")
        return entities
