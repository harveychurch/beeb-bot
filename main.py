import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv() 
bot = commands.Bot(command_prefix='!')
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")

for filename in os.listdir("modules"):
    if filename.endswith(".py"):
        filename_stripped = str(filename.strip(".py"))
        bot.load_extension("modules."+filename_stripped)
        print("Cog {0} has been loaded.".format(filename_stripped))


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


bot.run(SECRET_TOKEN)