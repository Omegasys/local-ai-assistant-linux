# action_executor.py
import logging

class ActionExecutor:
    def __init__(self):
        self.actions = {
            'open': self.open_file,
            'close': self.close_file,
            'calendar': self.show_calendar,
            'shutdown': self.shutdown_system,
        }

    def execute(self, user_input):
        """Execute an action based on the user input."""
        action = self.extract_action(user_input)
        if action:
            logging.info(f"Executing action: {action}")
            action(user_input)
        else:
            logging.warning("No valid action found for the input.")

    def extract_action(self, user_input):
        """Extract the action from the user input."""
        for action_key in self.actions:
            if action_key in user_input.lower():
                return self.actions[action_key]
        return None

    def open_file(self, user_input):
        """Open a file based on user input."""
        logging.info(f"Opening file as per the request: {user_input}")
        # Implement file-opening logic here

    def close_file(self, user_input):
        """Close a file based on user input."""
        logging.info(f"Closing file as per the request: {user_input}")
        # Implement file-closing logic here

    def show_calendar(self, user_input):
        """Show the calendar for the user."""
        logging.info("Showing the calendar.")
        # Implement calendar integration here

    def shutdown_system(self, user_input):
        """Shutdown the system."""
        logging.info("Shutting down the system.")
        # Implement shutdown logic here (careful with this in a real scenario!)
