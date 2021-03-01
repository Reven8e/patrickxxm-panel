


def main():
    try:
        global bot_token
        bot_token = open("bot_token.txt", "r")
        bot_token = bot_token.readlines()[0].strip()
    except IndexError:
        print("No Token at 'bot_token.txt'")
        return

    global guild_target