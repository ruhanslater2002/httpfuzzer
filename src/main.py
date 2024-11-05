from httpfuzzer import HttpFuzzer


class Main:
    def __init__(self):
        httpfuzzer: HttpFuzzer = HttpFuzzer("wordlists/namelist.txt", "http://google.com")
        httpfuzzer.fuzz_hidden_directories()


if __name__ == '__main__':
    Main()
