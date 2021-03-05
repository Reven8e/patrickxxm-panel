import time, sys, os
from colorama import Fore
from .auth import auth


class LogIn():
    def __init__(self):
        self.auth = auth()
        print(f"""
 ██ ▄█▀██▓██▓    ██▓   ▓█████▄▓█████  ██████▄▄▄█████▓██▀███  ▒█████▓██   ██▓
 ██▄█▒▓██▓██▒   ▓██▒   ▒██▀ ██▓█   ▀▒██    ▒▓  ██▒ ▓▓██ ▒ ██▒██▒  ██▒██  ██▒
▓███▄░▒██▒██░   ▒██░   ░██   █▒███  ░ ▓██▄  ▒ ▓██░ ▒▓██ ░▄█ ▒██░  ██▒▒██ ██░
▓██ █▄░██▒██░   ▒██░   ░▓█▄   ▒▓█  ▄  ▒   ██░ ▓██▓ ░▒██▀▀█▄ ▒██   ██░░ ▐██▓░
▒██▒ █░██░██████░██████░▒████▓░▒████▒██████▒▒ ▒██▒ ░░██▓ ▒██░ ████▓▒░░ ██▒▓░
▒ ▒▒ ▓░▓ ░ ▒░▓  ░ ▒░▓  ░▒▒▓  ▒░░ ▒░ ▒ ▒▓▒ ▒ ░ ▒ ░░  ░ ▒▓ ░▒▓░ ▒░▒░▒░  ██▒▒▒ 
░ ░▒ ▒░▒ ░ ░ ▒  ░ ░ ▒  ░░ ▒  ▒ ░ ░  ░ ░▒  ░ ░   ░     ░▒ ░ ▒░ ░ ▒ ▒░▓██ ░▒░ 
░ ░░ ░ ▒ ░ ░ ░    ░ ░   ░ ░  ░   ░  ░  ░  ░   ░       ░░   ░░ ░ ░ ▒ ▒ ▒ ░░  
░  ░   ░     ░  ░   ░  ░  ░      ░  ░     ░            ░        ░ ░ ░ ░     
                        ░                                           ░ ░     

""")
        print("\n")
        print(f"[1] Login.")
        print(f"[2] Exit.")
        self.option = int(input(": "))

    
    def login(self):
        user = input(f"Username: ")
        password = input("Password: ")

        if self.auth.Login(user, password) is True:
            print(f"[!] You have successfully logged in!")
            time.sleep(3)
            return True


    def start(self):
        if self.option == 1: 
            if self.login() is True:
                return True
        elif self.option == 2: 
            sys.exit(0)
    

def printer():
    print(f"""{Fore.LIGHTYELLOW_EX}

  ██████▄▄▄█████▓▄▄▄      ██▀███ ▄▄▄█████▓
▒██    ▒▓  ██▒ ▓▒████▄   ▓██ ▒ ██▓  ██▒ ▓▒
░ ▓██▄  ▒ ▓██░ ▒▒██  ▀█▄ ▓██ ░▄█ ▒ ▓██░ ▒░
  ▒   ██░ ▓██▓ ░░██▄▄▄▄██▒██▀▀█▄ ░ ▓██▓ ░ 
▒██████▒▒ ▒██▒ ░ ▓█   ▓██░██▓ ▒██▒ ▒██▒ ░ 
▒ ▒▓▒ ▒ ░ ▒ ░░   ▒▒   ▓▒█░ ▒▓ ░▒▓░ ▒ ░░   
░ ░▒  ░ ░   ░     ▒   ▒▒ ░ ░▒ ░ ▒░   ░    
░  ░  ░   ░       ░   ▒    ░░   ░  ░      
      ░               ░  ░  ░             
                                          
""")
    print(f"{Fore.BLUE}[CONSOLE] [0] Bot Nuker.")
    print("[CONSOLE] [1] Token Checker.")
    print("[CONSOLE] [2] Spammer")
    try:
        option = int(input(": "))
        return option
    except:
        print(f"\n{Fore.RED}[ERROR] Choose a number between 0-2!")
        time.sleep(4)
        sys.exit(0)


def main():
    if LogIn().start() is True:
        os.system("cls")
        def start():
            option = printer()
            if option == 0:
                try:
                    global bot_token
                    bot_token = open("bot_token.txt", "r")
                    bot_token = bot_token.readlines()[0].strip()
                except IndexError:
                    print(f"\n{Fore.RED}[ERROR] No Tokens In 'bot_token.txt'")
                    time.sleep(5)
                    return
                try:
                    from .nuker import nuker
                except ImportError:
                    time.sleep(4)
                    pass

            elif option == 1:
                from .token_checker import token_keker
                token_keker().start()

            elif option == 2:
                from .spammer import Spammer
                Spammer().start()

    start()
    while True:
        again = input(f'{Fore.BLUE}[CONSOLE] Anything else: ')
        if again == "y":
            os.system("cls")
            start()
        elif again == "no":
            print(f'\n{Fore.YELLOW}[CONSOLE] Oke mate cya!')
            break