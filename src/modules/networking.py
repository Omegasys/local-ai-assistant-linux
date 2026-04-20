# networking.py
import subprocess
import logging

class Networking:
    def __init__(self):
        pass

    def check_network_status(self):
        """Check the network connection status."""
        try:
            result = subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                logging.info("Network is connected.")
                return True
            else:
                logging.warning("Network is disconnected.")
                return False
        except Exception as e:
            logging.error(f"Error checking network status: {e}")
            return False

    def connect_to_wifi(self, ssid, password):
        """Connect to a WiFi network."""
        try:
            logging.info(f"Connecting to WiFi network: {ssid}")
            subprocess.run(["nmcli", "dev", "wifi", "connect", ssid, "password", password], check=True)
            logging.info(f"Successfully connected to {ssid}.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error connecting to WiFi network: {e}")

    def disconnect_wifi(self):
        """Disconnect from the current WiFi network."""
        try:
            subprocess.run(["nmcli", "dev", "disconnect", "wlan0"], check=True)
            logging.info("Disconnected from WiFi.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error disconnecting WiFi: {e}")
