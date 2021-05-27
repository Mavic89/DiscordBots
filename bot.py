import discord

import mysql.connector 

import json

import requests 

from discord.ext import commands

import random

import os

from requestium import Session, Keys

import re 

import mysql.connector 

from multiprocessing import Process

import subprocess

import whois

import hashlib

import time 

import socket

import nmap3



TOKEN = "NzY1MjU4MDI5NzY3MTk2NzMz.X4SMFA.-fWASZTlcIHuUbQnw1AN0R7-pbM"



bot = commands.Bot(command_prefix='?')



requestHeaders = {

    'Accept': 'application/json',

}



sess=Session(

    webdriver_path='/usr/local/bin/geckodriver',

    browser='phantomjs',

    default_timeout=20,

    webdriver_options={

        'arguments':['headless']

    }



)



mydb = mysql.connector.connect(

  host="localhost",

  user="root",

  password="orcus",

  database="xboxDB"

)





@bot.command()

async def email(ctx, arg):

      leakedCheckResponse = requests.get("https://leakcheck.net/api/?key=4f2b8074ad8f8e8fa9504afd0153f6b5bf21f6b1&check="+arg+"&type=email", headers=requestHeaders)

      leakedCheckJSON= leakedCheckResponse.json()



      deHashedResponse = requests.get('https://api.dehashed.com/search?query=email:'+arg, headers=requestHeaders, auth=('babayaga12344@gmail.com', 'acb3a2a4508c0c8398f6ba203fe746d4'))

      deHashedJSON=deHashedResponse.json()

      textFileString=""

      embedVar = discord.Embed(title="Orcus Results:", color=0xFF0000)

      try:

          for i in leakedCheckJSON["result"]:

              embedVar.add_field(name="Found:",value=i['line'],inline=False)

              textFileString+= i['line']+'\n'

      except:

           pass

      

      embedStrValue=""

      try:

        for i in range(0,len(deHashedJSON["entries"])):

            for j in deHashedJSON["entries"][i]:

                if (len(str(deHashedJSON["entries"][i][j])) > 1 and deHashedJSON["entries"][i][j] != None and str(j) != "id"):

                    embedStrValue+="**"+str(j).capitalize()+"**"+": "+str(deHashedJSON["entries"][i][j])+" "

                    textFileString+=str(j).capitalize()+": "+str(deHashedJSON["entries"][i][j])+"\n"

            embedVar.add_field(name="Found:", value=embedStrValue,inline=False) 

            embedStrValue=""

      except:

          pass

      try:

        await ctx.send(embed=embedVar)

      except:

          try:

                await ctx.send("Your response is too big! Creating Text File...")

                tfName=str(ctx.author.id)+str(round(random.randint(0,1000)))+".txt"

                textFile=open(tfName,"w+",encoding='utf-8')

                textFile.write(textFileString)

                textFile.close()

                await ctx.send(file=discord.File(tfName))

                if os.path.exists(tfName):

                        os.remove(tfName)

                textFileString=""

          except:

               await ctx.send("unknown error occured")

               textFileString=""





@bot.command()

async def tos(ctx):

    embedtos = discord.Embed(title="Terms of Service", color=0xFF0000)

    tos="""

    RULES



    • No spamming chat.

    • No racist or highly inappropriate language.

    • No disrespecting any staff members.

    • No referral links or discord invites.

    • We reserve the right to mute/ban you.

    • Rules are subject to change, as we may see fit.



    • We will not be held responsible for any unknown or miscellaneous purchases.

    • We will not be held responsible for any misuse of your personal information.

    • We will not be help responsible for any malicious activity with the info received from Orcus.

    """

    embedtos.add_field(name="Terms of Service for Orcus", value=tos,inline=False)

    await ctx.send(embed=embedtos) 



@bot.command()

async def orcushelp(ctx):

    embedHELP = discord.Embed(title="Terms of Service", color=0xFF0000)

    helpmsg="""

    • ?email <email>-perform an email search

    • ?phone <phone>-perform a phone number search

    • ?iplookup <ip>-find information on an ip address

    • ?ip <ip>-perform an ip address search

    • ?username <username>-perform a username search

    • ?xbox <gamertag>-perform an xbox search

    • ?crack <hash> <algorithm>-crack a hash(currently only md5, sha256, and sha512 supported)

    • ?who <domain>-perform a whois

    • ?portscan <ip/domain>-port scan a system(only scans the most popular ports)

    • ?tos-displays terms of service

    """

    embedHELP.add_field(name="Commands available", value=helpmsg,inline=False)

    await ctx.send(embed=embedHELP) 







@bot.command()

async def phone(ctx,arg):

      deHashedResponse = requests.get('https://api.dehashed.com/search?query=phone:'+arg, headers=requestHeaders, auth=('babayaga12344@gmail.com', 'acb3a2a4508c0c8398f6ba203fe746d4'))

      deHashedJSON=deHashedResponse.json()

      textFileString=""

      embedVar = discord.Embed(title="Orcus Results:", color=0xFF0000)

      embedStrValue=""

      try:

        for i in range(0,len(deHashedJSON["entries"])):

            for j in deHashedJSON["entries"][i]:

                if (len(str(deHashedJSON["entries"][i][j])) > 1 and deHashedJSON["entries"][i][j] != None and str(j) != "id"):

                    embedStrValue+="**"+str(j).capitalize()+"**"+": "+str(deHashedJSON["entries"][i][j])+" "

                    textFileString+=str(j).capitalize()+": "+str(deHashedJSON["entries"][i][j])+"\n"

            embedVar.add_field(name="Found:", value=embedStrValue,inline=False) 

            embedStrValue=""

      except:

          pass

      try:

        await ctx.send(embed=embedVar)

      except:

          try:

                await ctx.send("Your response is too big! Creating Text File...")

                tfName=str(ctx.author.id)+str(round(random.randint(0,1000)))+".txt"

                textFile=open(tfName,"w+",encoding='utf-8')

                textFile.write(textFileString)

                textFile.close()

                await ctx.send(file=discord.File(tfName))

                if os.path.exists(tfName):

                        os.remove(tfName)

                textFileString=""

          except:

               await ctx.send("unknown error occured")

               textFileString=""





@bot.command()

async def username(ctx,arg):

      deHashedResponse = requests.get('https://api.dehashed.com/search?query=username:'+arg, headers=requestHeaders, auth=('babayaga12344@gmail.com', 'acb3a2a4508c0c8398f6ba203fe746d4'))

      deHashedJSON=deHashedResponse.json()

      textFileString=""

      embedVar = discord.Embed(title="Orcus Results:", color=0xFF0000)

      embedStrValue=""

      try:

        for i in range(0,len(deHashedJSON["entries"])):

            for j in deHashedJSON["entries"][i]:

                if (len(str(deHashedJSON["entries"][i][j])) > 1 and deHashedJSON["entries"][i][j] != None and str(j) != "id"):

                    embedStrValue+="**"+str(j).capitalize()+"**"+": "+str(deHashedJSON["entries"][i][j])+" "

                    textFileString+=str(j).capitalize()+": "+str(deHashedJSON["entries"][i][j])+"\n"

            embedVar.add_field(name="Found:", value=embedStrValue,inline=False) 

            embedStrValue=""

      except:

          pass

      try:

        await ctx.send(embed=embedVar)

      except:

          try:

                await ctx.send("Your response is too big! Creating Text File...")

                tfName=str(ctx.author.id)+str(round(random.randint(0,1000)))+".txt"

                textFile=open(tfName,"w+",encoding='utf-8')

                textFile.write(textFileString)

                textFile.close()

                await ctx.send(file=discord.File(tfName))

                if os.path.exists(tfName):

                        os.remove(tfName)

                textFileString=""

          except:

               await ctx.send("unknown error occured")

               textFileString=""





@bot.command()

async def iplookup(ctx,arg):

    try:

      embedVar = discord.Embed(title="Orcus Results:", color=0xFF0000)

      ipstackResponse = requests.get('http://api.ipstack.com/'+arg+'?access_key=2d561b9600de56f57ba76984f56c5dd1')

      ipstackJSON=ipstackResponse.json()

      embedVar.add_field(name="Found:", value=ipstackJSON,inline=False) 

      await ctx.send(embed=embedVar)

    except:

        pass

        

@bot.command()

async def ip(ctx,arg):

      embedVar = discord.Embed(title="Orcus Results:", color=0xFF0000)

      deHashedResponse = requests.get('https://api.dehashed.com/search?query=ip_address:'+arg, headers=requestHeaders, auth=('babayaga12344@gmail.com', 'acb3a2a4508c0c8398f6ba203fe746d4'))

      deHashedJSON=deHashedResponse.json()

      textFileString=""

      embedStrValue=""

      try:

        for i in range(0,len(deHashedJSON["entries"])):

            for j in deHashedJSON["entries"][i]:

                if (len(str(deHashedJSON["entries"][i][j])) > 1 and deHashedJSON["entries"][i][j] != None and str(j) != "id"):

                    embedStrValue+="**"+str(j).capitalize()+"**"+": "+str(deHashedJSON["entries"][i][j])+" "

                    textFileString+=str(j).capitalize()+": "+str(deHashedJSON["entries"][i][j])+"\n"

            embedVar.add_field(name="Found:", value=embedStrValue,inline=False) 

            embedStrValue=""

      except:

          pass

      try:

        await ctx.send(embed=embedVar)

      except:

          try:

                await ctx.send("Your response is too big! Creating Text File...")

                tfName=str(ctx.author.id)+str(round(random.randint(0,1000)))+".txt"

                textFile=open(tfName,"w+",encoding='utf-8')

                textFile.write(textFileString)

                textFile.close()

                await ctx.send(file=discord.File(tfName))

                if os.path.exists(tfName):

                        os.remove(tfName)

                textFileString=""

          except:

               await ctx.send("unknown error occured")

               textFileString=""



@bot.command()

async def portscan(ctx,arg):

    try:

        nmap=nmap3.Nmap()

        result = nmap.scan_top_ports(arg)

        embedScan = discord.Embed(title="Port Scanner", color=0xdeecff)

        if(not(re.match("^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$",arg))):

            arg=socket.gethostbyname(arg)

    except:

        pass

    try:

        for i in range(0,str(result).count("protocol")):

            embedScan.add_field(name="Port Scan Results", value=result[arg]["ports"][i],inline=False)

            await ctx.send(embed=embedScan)

            embedScan.remove_field(0)

    except:

        pass





@bot.command()

async def crack(ctx,arg,arg2):

    embedCrack = discord.Embed(title="Hash Cracker", color=0x39138b)

    if(arg2.lower()=="md5"):

        with open("rockyou.txt","r",encoding='utf-8',errors="ignore") as hashfile:

            for line in hashfile:

                hash=hashlib.md5(line.strip().encode())

                if(hash.hexdigest()==arg):

                    embedCrack.add_field(name="Cracked:", value=line,inline=False)

                    await ctx.send(embed=embedCrack)

                    return

    if(arg2.lower()=="sha256"):

        with open("rockyou.txt","r",encoding='utf-8',errors="ignore") as hashfile:

            for line in hashfile:

                hash=hashlib.sha256(line.strip().encode())

                if(hash.hexdigest()==arg):

                    embedCrack.add_field(name="Cracked:", value=line,inline=False)

                    await ctx.send(embed=embedCrack)

                    return

    if(arg2.lower()=="sha512"):

        with open("rockyou.txt","r",encoding='utf-8',errors="ignore") as hashfile:

            for line in hashfile:

                hash=hashlib.sha512(line.strip().encode())

                if(hash.hexdigest()==arg):

                    embedCrack.add_field(name="Cracked:", value=line,inline=False)

                    await ctx.send(embed=embedCrack)

                    return





@bot.command()

async def xbox(ctx,arg):

    try:

        mycursor = mydb.cursor()

        embedxboxIP = discord.Embed(title="Xbox IP Resolve", color=0x15c534)

        sql="SELECT * FROM xboxUsers WHERE gamertag LIKE "+"'%"+arg+"%'"+";"

        mycursor.execute(sql)

        result=mycursor.fetchall()

        embedxboxIP.add_field(name="Found:", value=result[0],inline=False)

        await ctx.send(embed=embedxboxIP)

        return

    except:

        await ctx.send("Please try ?xbox2 for a more extensive search")









@bot.command()

async def who(ctx,arg):

    try:

        w=whois.query(arg)

        embedWhoIS=discord.Embed(title="Whois", color=0xf56420)

        embedWhoIS.add_field(name="Whois Information",value=w.__dict__,inline=False)

        await ctx.send(embed=embedWhoIS)

    except:

        await ctx.send("error occured")



async def on_message(self, message):

    if message.author == self.user:

        return





bot.run(TOKEN)



