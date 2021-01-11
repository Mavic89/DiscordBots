import discord
import mysql.connector 


mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)


TOKEN = ""
client = discord.Client()

@client.event
async def on_message(message):
    if("!sqlbot" in message.content):
          query = message.content[8:].strip()
          sqlq="SELECT * FROM ig WHERE name = "+"'"+query+"'"
          mycursor.execute(sqlq)
          result=mycursor.fetchall()
          await message.channel.send(result)


mycursor = mydb.cursor()
client.run(TOKEN)

