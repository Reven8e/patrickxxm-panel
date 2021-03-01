import discord, sys, random, string, os, time
from . import bot_token
from discord.ext import commands
from discord.utils import get

os.system("cls")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot is ready!\n\n")


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


print("[CONSOLE] [0] Exit.")
print("[CONSOLE] [1] Ban all users.")
print("[CONSOLE] [2] Kick all users.")
print("[CONSOLE] [3] Mass channel create.")
print("[CONSOLE] [4] Delete all channels.")
print("[CONSOLE] [5] Mass role create.")
print("[CONSOLE] [6] Delete all roles")

option = int(input("\n\n: "))
guild_target = int(input("\nServer target ID: "))

if option == 0:
    sys.exit()

elif option == 1:
    os.system("cls")
    print("starting...")
    time.sleep(3)
    ban_all(guild_target)
    print("Done!")

elif option == 2:
    os.system("cls")
    print("starting...")
    time.sleep(3)   
    kick_all(guild_target)

elif option == 3:
    am = int(input("Amount of channels to create (nums): "))
    os.system("cls")
    print("starting...")
    time.sleep(3)
    create_channels(guild_target, am)

elif option == 4:
    os.system("cls")
    print("starting...")
    time.sleep(3)
    delete_channels(guild_target)

elif option == 5:
    am = int(input("Amount of roles to create (nums): "))
    os.system("cls")
    print("starting...")
    time.sleep(3)
    create_roles(guild_target, am)

elif option == 6:
    os.system("cls")
    print("starting...")
    time.sleep(3)
    delete_roles(guild_target)


client.run(bot_token)