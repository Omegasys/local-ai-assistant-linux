# config.py
import json
import logging

class Config:
    @staticmethod
    def load_config():
        """Load configuration from a file or use defaults."""
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
            logging.info("Configuration loaded successfully.")
            return config
        except FileNotFoundError:
            logging.warning("Configuration file not found. Using default settings.")
            return Config.default_config()

    @staticmethod
    def default_config():
        """Return default configuration."""
        return {
            "speech_enabled": True,
            "logging_level": "DEBUG",
            "privacy_settings": {
                "data_encryption": True,
                "data_retention": 30  # days
            }
        }
