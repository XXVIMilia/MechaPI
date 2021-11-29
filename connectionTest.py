import os
import discord
from dotenv import load_dotenv

path = os.path.abspath(__file__)
path = path[:-(len(__file__)+8)]


load_dotenv(dotenv_path = path + "configFiles/.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to Discord!')
    for member in guild.members:
        print(member.name)

@client.event
async def on_message(message):
    test()
    print(message.content)
    
def test():
    print("This is a test")


client.run(TOKEN)