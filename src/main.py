from httpfuzzer import HttpFuzzer
import argparse
import sys
import os
from consolelogger import ConsoleLogger
import requests  # To handle network-related errors


def ascii_art():
    asciiart = r"""
___________                                 
\_   _____/_ __________________ ___________ 
 |    __)|  |  \___   /\___   // __ \_  __ \
 |     \ |  |  //    /  /    /\  ___/|  | \/
 \___  / |____//_____ \/_____ \\___  >__|   
     \/              \/      \/    \/       

    """
    return asciiart


class Main:
    def __init__(self, wordlist: str, url: str, threading: float):
        self.logger = ConsoleLogger("FUZZER")
        self.url = url
        self.wordlist = wordlist
        self.threading = threading

    def start(self) -> None:
        try:
            self.logger.info(f"Fuzzing: {self.url}, Threading in seconds: {self.threading}")
            http_fuzzer: HttpFuzzer = HttpFuzzer(self.wordlist, self.url, self.threading)
            http_fuzzer.fuzz_hidden_directories()
        except KeyboardInterrupt:
            self.logger.info("Fuzzing was interrupted by the user. Exiting...")
            sys.exit(0)  # Exit gracefully
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network-related error occurred: {e}")
            sys.exit(1)  # Exit with an error code
        except FileNotFoundError as e:
            self.logger.error(f"Wordlist file not found: {e}")
            sys.exit(1)  # Exit with an error code
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            sys.exit(1)  # Exit with an error code


def parse_args():
    parser = argparse.ArgumentParser(description="HTTP Fuzzer for hidden directories")
    parser.add_argument("-w", "--wordlist", type=str, default="wordlists/subdomains-top1million.txt",
                        help="Path to the wordlist file")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL to fuzz (e.g., http://example.com)")
    parser.add_argument("-t", "--threading", type=float, default=1, help="Threading delay in seconds (default: 1)")
    return parser.parse_args()


if __name__ == '__main__':
    print(ascii_art())
    # Parse the command-line arguments
    args = parse_args()

    # Validate wordlist file existence before proceeding
    if not os.path.exists(args.wordlist):
        print(f"[ERROR] Wordlist file '{args.wordlist}' does not exist.")
        sys.exit(1)

    # Create the Main instance with the arguments
    main = Main(args.wordlist, args.url, args.threading)
    # Start the fuzzing process
    main.start()
