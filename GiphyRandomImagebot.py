import os
import discord
import urllib.request
import json
import random

TOKEN = "###############"
GIPHYAPIKEY="#######################"
client = discord.Client()


@client.event
async def on_message(message):
    if(message.author == client.user):
        return

    if("!gifbot" in message.content):
        query = message.content[7:]
        url2Open="http://api.giphy.com/v1/gifs/search?q="+str("+".join(query.split()))+"&api_key="+GIPHYAPIKEY+"&limit=10"
        data = json.loads(urllib.request.urlopen(url2Open).read())
        await message.channel.send(data["data"][random.randint(1,10)-1]["images"]["original"]["url"])

client.run(TOKEN)
