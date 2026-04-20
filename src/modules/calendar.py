# calendar.py
import subprocess
import logging
import os
from datetime import datetime

class CalendarModule:
    def __init__(self):
        self.calendar_path = '/usr/bin/cal'  # Using the system's calendar tool (or another if preferred)

    def show_calendar(self):
        """Show the current month’s calendar."""
        try:
            logging.info("Displaying the current month calendar...")
            output = subprocess.check_output([self.calendar_path])
            print(output.decode())
        except subprocess.CalledProcessError as e:
            logging.error(f"Error displaying calendar: {e}")

    def add_event(self, event_details):
        """Add an event to the calendar."""
        # For simplicity, we assume the event_details are a string in a specific format
        event_command = f'echo "{event_details}" >> ~/calendar_events.txt'
        try:
            subprocess.run(event_command, shell=True, check=True)
            logging.info(f"Event added: {event_details}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error adding event: {e}")

    def view_events(self):
        """View saved events from the custom calendar file."""
        try:
            logging.info("Displaying saved events...")
            if os.path.exists('~/calendar_events.txt'):
                with open('~/calendar_events.txt', 'r') as f:
                    events = f.readlines()
                    for event in events:
                        print(event.strip())
            else:
                logging.warning("No events found.")
        except Exception as e:
            logging.error(f"Error viewing events: {e}")
