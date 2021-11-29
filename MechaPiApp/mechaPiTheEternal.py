from discord import client
from MechaPiApp.coreFeatures import clientClass
import os
import discord
from dotenv import load_dotenv
import asyncio
import signal


intents = discord.Intents.default()
intents.members = True
intents.messages = True

path = os.getcwd()
path = path[:-7]
load_dotenv(dotenv_path = path + "configFiles/.env")
discord.Client(intents = intents)


class MechaPiTheEternal:
    client = clientClass.ClientClass()
    loop = asyncio.get_event_loop()
    
    async def sendMessage(self,packet):
        print(packet)
        if(packet.author == self.client.user):
            return
        else:
            await packet.channel.send("This is a test")

    
    def __init__(self):
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.GUILD = os.getenv('DISCORD_GUILD')
        print("Ayo")

    def printText(self, *args):
        print("Helloooooooooooo")
        print(self.client.myData)
        self.loop.create_task(self.sendMessage(self.client.myData))
        

    def runBot(self):
        signal.signal(signal.SIGUSR1, self.printText)
        mainLoop = self.loop.create_task(self.client.start(self.TOKEN))
        self.loop.run_until_complete(mainLoop)