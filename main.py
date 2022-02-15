import discord
import platform
import os
from dotenv import load_dotenv


load_dotenv() 
client = discord.Client()
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello")

    if message.content.startswith('$BBC'):
        embed = discord.Embed(title="Video")
        await message.channel.send(embed=embed)

client.run(SECRET_TOKEN)