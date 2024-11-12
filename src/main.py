from httpfuzzer import HttpFuzzer
import argparse


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
        self.url = url
        self.wordlist = wordlist
        self.threading = threading

    def start(self) -> None:
        print(f"[*] Fuzzing: {self.url}, Threading in seconds: {self.threading}")
        http_fuzzer: HttpFuzzer = HttpFuzzer(self.wordlist, self.url, self.threading)
        http_fuzzer.fuzz_hidden_directories()


def parse_args():
    parser = argparse.ArgumentParser(description="HTTP Fuzzer for hidden directories")
    parser.add_argument("-w", "--wordlist", type=str, default="wordlists/subdomains-top1million.txt", help="Path to the wordlist file")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL to fuzz (e.g., http://example.com)")
    parser.add_argument("-t", "--threading", type=float, default=0, help="Threading delay in seconds (default: 0)")
    return parser.parse_args()


if __name__ == '__main__':
    print(ascii_art())

    # Parse the command-line arguments
    args = parse_args()

    # Create the Main instance with the arguments
    main = Main(args.wordlist, args.url, args.threading)

    # Start the fuzzing process
    main.start()
