import os

import discord
from dotenv import load_dotenv


responses = {"hey":"Hello Friend!"}
load_dotenv()
TOKEN = os.getenv('')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Hello {member.name} welcome to the server")


@client.event 
async def on_message(message):
    if(message.author==client.user):
        return
    
    def check(m):
        return m

    if "!pbot" in message.content:
        input = message.content[5:]
        foundresponse=False
        for i, k in enumerate(responses):
            if(input.strip().lower() in k.strip().lower() and foundresponse==False):
                await message.channel.send(responses[k])
                foundresponse=True
        if(foundresponse == False and input != responses[list(responses.keys())[-1]]):
            await message.channel.send("I dont know, what would you say to that?")
            reply = await client.wait_for('message',check=check)
            if(message.author==reply.author):
                responses[input] = reply.content
            else:
                await message.channel.send("I'm sorry "+str(message.author)+" can you say that again?")
                reply = await client.wait_for('message',check=check)
                responses[input] = reply.content
    
    else:
        msg = message.content
       
        if(not msg in responses and msg != responses[list(responses.keys())[-1]]):
            reply = await client.wait_for('message',check=check)
            if(message.author != reply.author):
                responses[msg] = reply.content


client.run(TOKEN)
