# speech_recognition.py
import speech_recognition as sr
import logging

class SpeechRecognition:
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.recognizer = sr.Recognizer()

    def listen(self):
        """Listen to user input through the microphone and recognize speech."""
        if not self.enabled:
            return None

        with sr.Microphone() as source:
            logging.info("Listening for input...")
            audio = self.recognizer.listen(source)

            try:
                # Recognizing speech using Google Web Speech API (could be replaced with offline methods)
                user_input = self.recognizer.recognize_google(audio)
                logging.info(f"Recognized speech: {user_input}")
                return user_input
            except sr.UnknownValueError:
                logging.error("Could not understand the audio")
                return None
            except sr.RequestError:
                logging.error("Could not request results from speech recognition service")
                return None
