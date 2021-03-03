import time, sys, os
from colorama import Fore
from .auth import auth


class LogIn():
    def __init__(self):
        self.auth = auth()

        print(f"{Fore.BLUE}[1] Login.")
        print(f"{Fore.BLUE}[2] Exit.")
        self.option = int(input(": "))

    
    def login(self):
        user = input(f"{Fore.CYAN}Username: ")
        password = input(f"{Fore.CYAN}Password: ")

        if self.auth.Login(user, password) is True:
            print(f"{Fore.YELLOW}[!] {Fore.WHITE}You have successfully logged in!")
            time.sleep(3)
            return True 


    def start(self):
        if self.option == 1: 
            if self.login() is True:
                return True
        elif self.option == 2: 
            sys.exit(0)
    

def printer():
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
        option = printer()
        if option == 0:
            try:
                global bot_token
                bot_token = open("bot_token.txt", "r")
                bot_token = bot_token.readlines()[0].strip()
            except IndexError:
                print(f"\n{Fore.RED}[ERROR] No Tokens In 'bot_token.txt'")
                return
            try:
                from .nuker import nuker
            except ImportError:
                pass
        
        elif option == 1:
            from .token_checker import token_keker
            token_keker().start()

        elif option == 2:
            from .spammer import Spammer
            Spammer().start()