from httpfuzzer import HttpFuzzer


class Main:
    def __init__(self):
        httpfuzzer: HttpFuzzer = HttpFuzzer("wordlists/subdomains-top1million.txt", "http://192.168.253.134")
        httpfuzzer.fuzz_hidden_directories()


if __name__ == '__main__':
    Main()
