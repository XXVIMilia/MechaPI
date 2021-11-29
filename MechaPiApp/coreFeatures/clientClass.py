import asyncio
import discord
import signal
import os


class ClientClass(discord.Client):
    myData = ""
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        self.myData = "On ready"
        

    async def on_message(self,message):
        print("message recieved")
        self.myData = message
        os.kill(os.getpid(), signal.SIGUSR1)

    

