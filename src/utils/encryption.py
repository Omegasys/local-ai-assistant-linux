# encryption.py
from cryptography.fernet import Fernet
import logging

class Encryption:
    def __init__(self):
        """Generate and store a symmetric key for encryption."""
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        logging.info("Encryption key generated and ready.")

    def encrypt(self, data):
        """Encrypt data."""
        if isinstance(data, str):
            data = data.encode()  # Convert string to bytes
        encrypted_data = self.cipher_suite.encrypt(data)
        logging.info("Data encrypted successfully.")
        return encrypted_data

    def decrypt(self, encrypted_data):
        """Decrypt data."""
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        logging.info("Data decrypted successfully.")
        return decrypted_data.decode()  # Return as string

    def save_key(self, file_path='secret.key'):
        """Save the encryption key to a file."""
        with open(file_path, 'wb') as key_file:
            key_file.write(self.key)
        logging.info(f"Encryption key saved to {file_path}.")

    def load_key(self, file_path='secret.key'):
        """Load an encryption key from a file."""
        with open(file_path, 'rb') as key_file:
            self.key = key_file.read()
            self.cipher_suite = Fernet(self.key)
        logging.info(f"Encryption key loaded from {file_path}.")
