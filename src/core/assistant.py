# assistant.py
import logging
from .action_executor import ActionExecutor
from .privacy_manager import PrivacyManager
from .speech_recognition import SpeechRecognition
from .config import Config

class Assistant:
    def __init__(self):
        self.config = Config.load_config()
        self.action_executor = ActionExecutor()
        self.privacy_manager = PrivacyManager()
        self.speech_recognition = SpeechRecognition(self.config['speech_enabled'])

        logging.basicConfig(level=logging.DEBUG)

    def start(self):
        """Start the assistant and wait for user input."""
        logging.info("Starting the AI Assistant...")

        while True:
            user_input = self.get_user_input()

            if user_input:
                self.process_input(user_input)

    def get_user_input(self):
        """Get user input either via speech or text."""
        if self.config['speech_enabled']:
            return self.speech_recognition.listen()
        else:
            return input("How can I assist you? ")

    def process_input(self, user_input):
        """Process the user input and perform action."""
        logging.info(f"Processing input: {user_input}")
        
        # Apply privacy measures first
        if not self.privacy_manager.is_input_safe(user_input):
            logging.warning("Input violated privacy rules. Ignoring request.")
            return

        # Perform the action based on the input
        self.action_executor.execute(user_input)
