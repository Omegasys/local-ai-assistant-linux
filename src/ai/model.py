# model.py
import pickle
import logging

class Model:
    def __init__(self, model_path=None):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        """Load a pre-trained machine learning model."""
        try:
            if self.model_path:
                with open(self.model_path, 'rb') as model_file:
                    self.model = pickle.load(model_file)
                    logging.info(f"Model loaded from {self.model_path}.")
            else:
                logging.warning("Model path is not provided.")
        except Exception as e:
            logging.error(f"Error loading model: {e}")
        
    def save_model(self):
        """Save the trained model to a file."""
        try:
            with open(self.model_path, 'wb') as model_file:
                pickle.dump(self.model, model_file)
                logging.info(f"Model saved to {self.model_path}.")
        except Exception as e:
            logging.error(f"Error saving model: {e}")
        
    def predict(self, data):
        """Make predictions using the pre-trained model."""
        if self.model:
            try:
                prediction = self.model.predict([data])
                logging.info(f"Prediction: {prediction}")
                return prediction
            except Exception as e:
                logging.error(f"Error during prediction: {e}")
                return None
        else:
            logging.error("Model is not loaded.")
            return None
