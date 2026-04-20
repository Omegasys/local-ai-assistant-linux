# web_search.py
import subprocess
import logging

class WebSearch:
    def __init__(self):
        pass

    def search(self, query):
        """Perform a web search using the default browser."""
        try:
            logging.info(f"Searching for: {query}")
            search_url = f"https://www.google.com/search?q={query}"
            subprocess.run(["xdg-open", search_url])
        except Exception as e:
            logging.error(f"Error performing web search: {e}")
