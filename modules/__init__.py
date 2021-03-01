from colorama import Fore

def printer():
    print("[CONSOLE] [0] Bot Nuker.")
    print("[CONSOLE] [1] Spammer.")
    option = int(input(": "))
    return option


def main():
    option = printer()

    if option == 0:
        try:
            global bot_token
            bot_token = open("bot_token.txt", "r")
            bot_token = bot_token.readlines()[0].strip()
        except IndexError:
            print("\nNo Token at 'bot_token.txt'")
            return
        from .nuker import nuker