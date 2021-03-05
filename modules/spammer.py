import requests, time, sys, json, emojis, os, threading, random
from colorama import Fore


class Spammer():
    def __init__(self):
        os.system("cls")
        print(f"""{Fore.MAGENTA}

  ██████ ██▓███  ▄▄▄      ███▄ ▄███▓███▄ ▄███▓█████ ██▀███  
▒██    ▒▓██░  ██▒████▄   ▓██▒▀█▀ ██▓██▒▀█▀ ██▓█   ▀▓██ ▒ ██▒
░ ▓██▄  ▓██░ ██▓▒██  ▀█▄ ▓██    ▓██▓██    ▓██▒███  ▓██ ░▄█ ▒
  ▒   ██▒██▄█▓▒ ░██▄▄▄▄██▒██    ▒██▒██    ▒██▒▓█  ▄▒██▀▀█▄  
▒██████▒▒██▒ ░  ░▓█   ▓██▒██▒   ░██▒██▒   ░██░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ▒▓▒░ ░  ░▒▒   ▓▒█░ ▒░   ░  ░ ▒░   ░  ░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░▒ ░      ▒   ▒▒ ░  ░      ░  ░      ░░ ░  ░ ░▒ ░ ▒░
░  ░  ░ ░░        ░   ▒  ░      ░  ░      ░     ░    ░░   ░ 
      ░               ░  ░      ░         ░     ░  ░  ░     
                                                            

""")
        print(f"{Fore.BLUE}[CONSOLE] [0] Go Back.")
        print(f"{Fore.BLUE}[CONSOLE] [1] Joiner.")
        print(f"{Fore.BLUE}[CONSOLE] [2] Leaver.")
        print(f"{Fore.BLUE}[CONSOLE] [3] Server Spammer / DM Spammer.")
        print(f"{Fore.BLUE}[CONSOLE] [4] Reaction Spammer.")
        print(f"{Fore.BLUE}[CONSOLE] [5] Friend Request Spammer.")
        print(f"{Fore.BLUE}[CONSOLE] [6] Unfriender.")
        try:
            self.option = int(input(": "))
        except:
            print(f"\n{Fore.RED}[ERROR] Choose a number between 0-6!")
            time.sleep(4)
            sys.exit(0)

        self.JOINER = "https://discordapp.com/api/invites/" #POST
        self.LEAVER = "https://discord.com/api/users/@me/guilds/" #DELETE
        self.SPAMMER = "https://discord.com/api/channels/" #POST
        # messages POST: https://discord.com/api/channels/CHANNEL.ID/messages
        # create reacton PUT: https://discord.com/api/channels/CHANNEL.ID/messages/MESSAGE.ID/reactions/emoji/@me
        # all reactions GET: https://discord.com/api/channels/{channel.id}/messages/{message.id}/reactions/{emoji}
        self.FRIEND_REQUESTER = "https://discord.com/api/users/@me/relationships"

        self.total = 0
        self.bad = 0
        self.success = 0
        self.missing_permission = 0
        self.missing_access = 0
        self.verbose = True
    

    def joiner(self, token, code):
        headers = {"Authorization": token,
            "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Content-Type": "application/json"}

        url = f"{self.JOINER}{code}"
        r = requests.post(url, headers=headers)

        if "id" in r.text:
            print("Joined")
        elif "Missing Permissions" in r.text:
            print("Missing Permission")
            return
        elif "Missing Access" in r.text:
            print("Missing Access")
            return
        else:
            print("Can't Join")
            return
    

    def leaver(self, token, guild_id):
        headers = {"Authorization": token,
            "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
        
        url = f"{self.LEAVER}{guild_id}"
        r = requests.delete(url, headers=headers)

        if "id" in r.text:
            self.success += 1
        elif "Missing Permissions" in r.text:
            self.missing_permission += 1
            return
        elif "Missing Access" in r.text:
            self.missing_access += 1
            return
        else:
            self.bad += 1
            return

    def spammer(self, token, obj_id, message, targ):
        headers = {"Authorization": token,
            "Content-Type": "application/json"}
        data = json.dumps({"content": message})
        self.total += 1

        if targ == "dm":
            recipents = json.dumps({"recipients": [obj_id]})
            re = requests.post(f"https://discord.com/api/users/@me/channels", headers=headers, data=recipents)

            if "id" in re.text:
                self.success += 1
                body = re.json()
                body = body["id"]
            elif "Missing Permissions" in re.text:
                self.missing_permission += 1
                return
            elif "Missing Access" in re.text:
                self.missing_access += 1   
                return  
            else:
                self.bad += 1
                return

        url = f"{self.SPAMMER}{body}/messages"
        r = requests.post(url, headers=headers, data=data)

        if obj_id in r.text:
            self.success += 1
        elif "Missing Permissions" in r.text:
            self.missing_permission += 1
        elif "Missing Access" in r.text:
            self.missing_access += 1     
        else:
            self.bad += 1

    
    def reactioner(self, token, channel_id, message_id, Emoji, add):
        headers = {"Authorization": token,
            "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}
        self.total += 1

        emo = emojis.encode(Emoji)
        url = f"{self.SPAMMER}{channel_id}/messages/{message_id}/reactions/{emo}/@me"
        
        if add == "remove":
            r = requests.delete(url, headers=headers)
        else:
            r = requests.put(url, headers=headers)
        if r.text == "":
            self.success += 1
        elif "Missing Permissions" in r.text:
            self.missing_permission += 1
        elif "Missing Access" in r.text:
            self.missing_access += 1     
        else:
            self.bad += 1

    
    def friender(self, token, user, tag):
        headers = {"Authorization": token,
            "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Content-Type": "application/json"}
        data = json.dumps({"username":user, "discriminator":tag})
        self.total += 1

        r = requests.post(self.FRIEND_REQUESTER, headers=headers, data=data)

        if r.text == "":
            self.success += 1
        elif "Missing Permissions" in r.text:
            self.missing_permission += 1
        elif "Missing Access" in r.text:
            self.missing_access += 1     
        else:
            self.bad += 1


    def unfriender(self, token, user_id):
        headers = {"Authorization": token,
            "User-Agent" :"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Content-Type": "application/json"}
        self.total += 1

        url = f"{self.FRIEND_REQUESTER}{user_id}"
        r = requests.post(url, headers=headers)

        if r.text == "":
            self.success += 1
        elif "Missing Permissions" in r.text:
            self.missing_permission += 1
        elif "Missing Access" in r.text:
            self.missing_access += 1     
        else:
            self.bad += 1
        
    def screen(self):
        os.system("cls")
        print(f"{Fore.GREEN}Sucesses: {self.success}")
        print(f"{Fore.BLUE}Missing Access (ban/not in server/cooldown): {self.missing_access}")
        print(f"{Fore.RED}Missing Permission: {self.missing_permission}")
        print(f"{Fore.RED}Bads: {self.bad}")
        print(f"{Fore.YELLOW}Total: {self.total}")
        time.sleep(3)
        if self.verbose == True:
            threading.Thread(target=self.screen, args=()).start()


    def start(self):
        if self.option == 0:
            return

        tokens = open("tokens_valid.txt")
        tokens = [token.strip() for token in tokens]
        delay = float(input(f"{Fore.BLUE}[CONSOLE] Please enter delay (0.01-2 secs): "))

        if self.option == 1:
            inv = input(f"{Fore.CYAN} Enter invite code (only code): ")

            for token in tokens:   
                threading.Thread(target=self.joiner, args=(token, inv,)).start()
                time.sleep(delay)
            time.sleep(3)
            self.verbose = False
            return
            
        elif self.option == 2:
            server_id = input(f"{Fore.CYAN}[CONSOLE] Server ID: ")
            self.screen()

            for token in tokens: 
                threading.Thread(target=self.leaver, args=(token, server_id,))             
                time.sleep(delay)
            time.sleep(3)
            self.verbose = False
            return
        
        elif self.option == 3:
            opt = input(f"{Fore.CYAN}DM or Server spammer? (dm/server): ")
            if opt == "server": target = input(f"{Fore.CYAN}Server's Channel ID: ")
            elif opt == "dm": target = input(f"{Fore.CYAN}User's ID: ")
            message = input(f"{Fore.CYAN}Message: ")
            much = int(input(f"{Fore.CYAN}How much time to work (10-100 secs): "))
            self.screen()

            th = threading.Thread(target=time.sleep, args=(much,))
            th.start()
            while True:
                if not th.is_alive():
                    self.verbose = False
                    time.sleep(3)
                    print(f"{Fore.YELLOW}[CONSOLE] Time's up, Closing...")
                    time.sleep(2)
                    return
                if threading.active_count() < 20:
                    threading.Thread(target=self.spammer, args=(random.choice(tokens), target, message, opt,)).start()
                    time.sleep(delay)

        elif self.option == 4:
            channel = input(f"{Fore.CYAN}Server's Channel ID: ")
            target = input(f"{Fore.CYAN}Message ID: ")
            emoj = input(f"{Fore.CYAN}Emoji (name) (REGULAR ONLY!): ")
            add = input(f"{Fore.CYAN}Add or Remove? (add/remove): ")
            self.screen()

            for token in tokens:
                self.reactioner(random.choice(tokens), channel, target, emoj, add)
                time.sleep(delay)
            time.sleep(3)
            self.verbose = False
            return

        elif self.option == 5:
            user = input(f"{Fore.CYAN}User Name (without tag): ")
            tag = int(input(f"{Fore.CYAN}User's Tag (without #): "))
            self.screen()

            for token in tokens:  
                threading.Thread(target=self.friender, args=(token, user, tag,)).start()
                time.sleep(delay)
            time.sleep(3)
            self.verbose = False
            return

        elif self.option == 6:
            user = input(f"{Fore.CYAN}User's ID: ")
            self.screen()

            for token in tokens: 
                threading.Thread(target=self.friender, args=(token, user)) 
                time.sleep(delay)
            time.sleep(3)
            self.verbose = False
            return



# Spammer().joiner("NzU2NzIzNDEyMTU1NzYwNzIy.X6GuLA.vFVgr3R-kT-R-p5ENTKOm_yCTPo", "9KWekzCa")
# Spammer().spammer("NzU2NzIzNDEyMTU1NzYwNzIy.X6GuLA.vFVgr3R-kT-R-p5ENTKOm_yCTPo", "655019591927595048", "hello")
# Spammer().reactioner("NzU2NzIzNDEyMTU1NzYwNzIy.X6GuLA.vFVgr3R-kT-R-p5ENTKOm_yCTPo", "655019591927595048", "806974125578911804", ":grinning:", "y", "remove")
# Spammer().friender("NzU2NzIzNDEyMTU1NzYwNzIy.X6GuLA.vFVgr3R-kT-R-p5ENTKOm_yCTPo", "Reven8e.sh", 9290)