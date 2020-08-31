import discord
from datetime import datetime 
import time
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

TOKEN = ""
client = discord.Client()


@client.event
async def on_message(message):
    if(message.author == client.user):
        return

    if("!help" in message.content):
        await message.channel.send("Type !setalarm 00:00 to set your alarm.")

    if("!setalarm" in message.content):
        alarmTime = message.content[9:].strip()
        print("alarm set to go off at",alarmTime)
        foobar=True
        while(foobar==True):
            x= datetime.now().strftime("%H")
            y=int(x)
            if(y > 12 ):
                z=abs(y-12)
            else:
                z=y
            m=str(z)+":"+datetime.now().strftime("%M")
            if(alarmTime==m):
                await message.channel.send("Time to wake up!")
                path = r"alarm sound file"
                channel=message.author.voice.channel
                vc = await channel.connect()

                vc.play(discord.FFmpegPCMAudio(path))
                while vc.is_playing():
                    continue
                
                await vc.disconnect(force=True)
                foobar=False
        
        

client.run(TOKEN)
