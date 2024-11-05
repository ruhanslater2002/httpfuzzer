from httphandler import HttpHandler
from termcolor import colored
import time


class HttpFuzzer:
    def __init__(self, wordlist: str, url: str):
        # Init colors
        self.plus = colored("+", "green")
        self.minus = colored("-", "red")

        self.wordlist = wordlist
        self.url = url

    def fuzz_hidden_directories(self):
        with open(self.wordlist, "r") as wordlist:
            for word in wordlist:
                word = word.strip()  # Use the assignment to strip whitespace
                if not word:  # Skip empty lines
                    continue

                # Combines url and word
                full_url = f"{self.url}/{word}"

                # Creates the instance with the combined word
                httphandler: HttpHandler = HttpHandler(full_url)
                try:
                    # Gets status code from combined url
                    time.sleep(0.3)  # Introduce a delay
                    response = httphandler.get_status_code()  # Make sure this matches your method
                    if response == 200:
                        print(f"[{self.plus}] Response {response} from {full_url}")
                except:
                    continue
