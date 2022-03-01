from http.client import responses
from discord.ext import commands
from discord_slash import cog_ext
from discord import Embed
import subprocess
import requests
class GitInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(description="Prints the current git SHA the bot is running!",name="version")
    async def version(self, ctx):
       label = str(subprocess.check_output(["git", "rev-parse","--short","HEAD"])).strip("b'")
       label = label[:label.index("\\")] 
       embed = Embed(title="The current version is: {0}".format(label))
       await ctx.send(embed=embed)

    @cog_ext.cog_slash(description="How to contribute to the project!",name="contribute")
    async def contribute(self,ctx):
        await ctx.send("You can contribute at https://github.com/harveychurch/beeb-bot")

    @cog_ext.cog_slash(description="How to contribute to the project!",name="stats")    
    async def stats(self,ctx):
        header = {"Accept": "application/vnd.github.v3+json"}
        try:
            response = requests.get(headers=header,url="https://api.github.com/repos/harveychurch/beeb-bot")
            await ctx.send(response)
        except:
            ctx.send("Error Retrieving Stats from GitHub")


def setup(bot):
    bot.add_cog(GitInfo(bot))