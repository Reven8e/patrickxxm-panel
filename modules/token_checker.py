import requests, time, threading, os
from colorama import Fore

class token_keker():
    def __init__(self):
        self.url = "https://discordapp.com/api/users/@me"
        os.system("cls")
        print(f"""{Fore.YELLOW}

 ▄████▄  ██░ ██▓█████ ▄████▄  ██ ▄█▓█████ ██▀███  
▒██▀ ▀█ ▓██░ ██▓█   ▀▒██▀ ▀█  ██▄█▒▓█   ▀▓██ ▒ ██▒
▒▓█    ▄▒██▀▀██▒███  ▒▓█    ▄▓███▄░▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██░▓█ ░██▒▓█  ▄▒▓▓▄ ▄██▓██ █▄▒▓█  ▄▒██▀▀█▄  
▒ ▓███▀ ░▓█▒░██░▒████▒ ▓███▀ ▒██▒ █░▒████░██▓ ▒██▒
░ ░▒ ▒  ░▒ ░░▒░░░ ▒░ ░ ░▒ ▒  ▒ ▒▒ ▓░░ ▒░ ░ ▒▓ ░▒▓░
  ░  ▒   ▒ ░▒░ ░░ ░  ░ ░  ▒  ░ ░▒ ▒░░ ░  ░ ░▒ ░ ▒░
░        ░  ░░ ░  ░  ░       ░ ░░ ░   ░    ░░   ░ 
░ ░      ░  ░  ░  ░  ░ ░     ░  ░     ░  ░  ░     
░                    ░                            

""")
        print("\n")
        self.checked = 0
        self.unverifed = 0
        self.bad = 0
        self.good = 0
        self.verbose = True

    def check(self, token):
        headers={
            'Authorization': token
        }
        r = requests.get(self.url, headers=headers)

        if "You need to verify your account in order to perform this action." in r.text:
            self.unverifed += 1

        elif "Unauthorized" in r.text:
            self.bad += 1
        
        elif "Access denied" in r.text:
            self.bad += 1

        else:
            self.good += 1
            with open("tokens_valid.txt", "a+", encoding="utf-8", errors='ignore') as f:
                f.write(f"{token}\n")
        

    def screen(self):
        os.system("cls")
        print(f"{Fore.GREEN}Good Tokens: {self.good}")
        print(f"{Fore.BLUE}Unverified Tokens: {self.unverifed}")
        print(f"{Fore.RED}Bad Tokens: {self.bad}")
        print(f"{Fore.YELLOW}Total Checked Tokens: {self.checked}")
        time.sleep(3)
        if self.verbose == True:
            threading.Thread(target=self.screen, args=()).start()


    def start(self):
        print(f"{Fore.CYAN} [1] Go Back.")
        print(f"{Fore.CYAN} [2] Start.")
        option = int(input(": "))
        if option == 1:
            return

        elif option == 2:
            tokens = open("tokens.txt", "r", encoding="utf-8", errors='ignore')
            tokens = [token.strip() for token in tokens]
            length = len(tokens)
            if len(tokens) == 0:
                print(f"{Fore.RED}[CONSOLE] No tokens found!")
                time.sleep(5)
                return
            threads = []
            self.screen()

            while True:
                if self.checked < length:
                    if threading.active_count() < int(10):
                        t = threading.Thread(target=self.check, args=(tokens[self.checked],))
                        t.start()
                        threads.append(t)
                        self.checked += 1

                else:
                    time.sleep(15)
                    self.verbose = False
                    print(f"\n\n{Fore.YELLOW}[CONSOLE] CLOSING!\nReopen the program to start checking! Btw open tokens_valid to get all valid tokens.")
                    time.sleep(3)
                    return
