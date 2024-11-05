from httpfuzzer import HttpFuzzer


def ascii_art():
    asciiart = r"""
___________                                 
\_   _____/_ __________________ ___________ 
 |    __)|  |  \___   /\___   // __ \_  __ \
 |     \ |  |  //    /  /    /\  ___/|  | \/
 \___  / |____//_____ \/_____ \\___  >__|   
     \/              \/      \/    \/       
                By: IntegerType
    """
    return asciiart


class Main:
    def __init__(self, wordlist: str, url: str, threading: float):
        self.url = url
        self.wordlist = wordlist
        self.threading = threading

    def start(self):
        print(f"[*] Fuzzing: {self.url}, Threading in seconds: {self.threading}")
        httpfuzzer: HttpFuzzer = HttpFuzzer(self.wordlist, self.url, self.threading)
        httpfuzzer.fuzz_hidden_directories()


if __name__ == '__main__':
    print(ascii_art())
    Main("wordlists/subdomains-top1million.txt", "http://192.168.253.134", 0).start()
