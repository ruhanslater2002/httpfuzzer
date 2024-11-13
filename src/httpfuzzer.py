from httphandler import HttpHandler
from termcolor import colored
import time
from typing import List
from consolelogger import ConsoleLogger
import threading


class HttpFuzzer:
    def __init__(self, wordlist: str, url: str, threading_delay: float, max_threads: int = 10):
        self.logger = ConsoleLogger("FUZZER")
        self.wordlist = wordlist
        self.url = url
        self.threading_delay = threading_delay
        self.max_threads = max_threads  # Max number of threads to run concurrently

    def fuzz_hidden_directories(self):
        wordlist: List[str] = self.load_wordlist()

        # Create a thread pool with a limited number of threads
        threads: threading = []
        for word in wordlist:
            word = word.strip()  # Use the assignment to strip whitespace
            if not word:  # Skip empty lines
                continue
            # Combines url and word
            full_url: str = self.url + "/" + word
            # Create a thread for each URL
            thread = threading.Thread(target=self.fuzz_url, args=(full_url,))
            threads.append(thread)
            # Start the thread
            thread.start()

            # Limit the number of concurrent threads
            if len(threads) >= self.max_threads:
                # Wait for all threads to complete before starting new ones
                for t in threads:
                    t.join()
                threads = []

        # Wait for any remaining threads to finish
        for thread in threads:
            thread.join()

    def fuzz_url(self, full_url: str):
        http_handler: HttpHandler = HttpHandler(full_url)
        try:
            time.sleep(self.threading_delay)  # Introduce a delay between requests
            try:
                response: int = http_handler.get_status_code()  # Gets status code from combined URL
            except Exception as e:
                self.logger.info(f"Fuzzing error: {colored(full_url, 'red')}, error: {e}")
                time.sleep(30)  # Waits 30 seconds if too many requests
                response = http_handler.get_status_code()
            if response == 200:
                self.logger.info(f"Response {response} from {colored(full_url, 'green')}")
        except KeyboardInterrupt:
            self.logger.error(f"Fuzzing canceled.")

    def load_wordlist(self) -> List[str]:
        with open(self.wordlist, "r") as wordlist:
            return wordlist.readlines()  # Return all lines as a list of strings
