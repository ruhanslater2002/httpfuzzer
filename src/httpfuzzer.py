from httphandler import HttpHandler
from termcolor import colored
import time
from typing import List
from consolelogger import ConsoleLogger


class HttpFuzzer:
    def __init__(self, wordlist: str, url: str, threading: float):
        self.logger = ConsoleLogger("FUZZER")
        self.wordlist = wordlist
        self.url = url
        self.threading = threading

    def fuzz_hidden_directories(self):
        wordlist: List[str] = self.load_wordlist()
        for word in wordlist:
            word = word.strip()  # Use the assignment to strip whitespace
            if not word:  # Skip empty lines
                continue
            # Combines url and word
            full_url = f"{self.url}/{word}"
            # Creates the instance with the combined word
            http_handler: HttpHandler = HttpHandler(full_url)
            try:
                time.sleep(self.threading)  # Introduce a delay
                try:
                    response = http_handler.get_status_code()  # Gets status code from combined URL
                except Exception as e:
                    self.logger.info(f"Fuzzing error: {colored(full_url, 'red')}, error: {e}")
                    time.sleep(30)  # Waits 30 seconds if too many requests
                    response = http_handler.get_status_code()
                if response == 200:
                    self.logger.info(f"Response {response} from {colored(full_url, 'green')}")
            except KeyboardInterrupt:
                self.logger.error(f"Fuzzing canceled.")
                break

    def load_wordlist(self) -> List[str]:
        with open(self.wordlist, "r") as wordlist:
            return wordlist.readlines()  # Return all lines as a list of strings
