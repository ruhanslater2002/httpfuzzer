from httphandler import HttpHandler
from termcolor import colored


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
                word.strip()
                # Combines url and word
                self.url = self.url + '/' + word
                # Creates the instance with the combined word
                httphandler: HttpHandler = HttpHandler(self.url)
                try:
                    # Gets status code from combined url
                    response: int = httphandler.get_status_code()
                    if response == 200:
                        print(f"[{self.plus}] Response {response} from {self.url}")
                    # else:
                    #     print(f"[{self.plus}] Response {response} from {self.url}")
                except Exception as e:
                    print(f"[{self.minus}] Error: {e}")
