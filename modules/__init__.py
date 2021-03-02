import time, sys
from colorama import Fore

def printer():
    print("[CONSOLE] [0] Bot Nuker.")
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