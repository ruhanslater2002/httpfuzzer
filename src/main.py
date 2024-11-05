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
    def __init__(self, wordlist: str, url: str):
        self.url = url
        self.wordlist = wordlist

    def start(self):
        print(f"[*] Fuzzing {self.url}")
        httpfuzzer: HttpFuzzer = HttpFuzzer(self.wordlist, self.url)
        httpfuzzer.fuzz_hidden_directories()


if __name__ == '__main__':
    print(ascii_art())
    Main("wordlists/subdomains-top1million.txt", "http://192.168.253.134").start()
