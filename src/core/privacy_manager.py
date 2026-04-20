# privacy_manager.py
import logging

class PrivacyManager:
    def __init__(self):
        self.privacy_rules = self.load_privacy_rules()

    def load_privacy_rules(self):
        """Load privacy rules to ensure data safety."""
        # These can be more complex rules based on your requirements
        rules = {
            "no_external_data": True,
            "input_encryption": True,
        }
        return rules

    def is_input_safe(self, user_input):
        """Check if the user input adheres to privacy rules."""
        logging.debug(f"Checking privacy for input: {user_input}")

        # Implement privacy rules here. For simplicity, we just check if the rule 'no_external_data' is violated
        if self.privacy_rules.get('no_external_data') and "send" in user_input:
            return False
        return True

    def encrypt_data(self, data):
        """Encrypt sensitive data before saving or processing."""
        # Simple encryption logic (just for demonstration; should be more complex in real use)
        encrypted_data = data[::-1]  # Reverse the string as a dummy encryption method
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypt the encrypted data."""
        return encrypted_data[::-1]  # Reverse again to get the original data
