from httphandler import HttpHandler


class HttpFuzzer:
    def __init__(self, directory: str, url: str):
        self.directory = directory
        self.url = url

    def fuzz_hidden_directories(self):
        with open(self.directory, "r") as wordlist:
            for word in wordlist:
                word.strip()
                self.url = self.url + '/' + word
                httphandler: HttpHandler = HttpHandler(self.url)
                try:
                    response: int = httphandler.get_status_code()
                    if response == 200:
                        print(f"[+] Response from {self.url}")
                except Exception as e:
                    print(f"[-] Error: {e}")
