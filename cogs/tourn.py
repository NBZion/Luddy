import discord
import json
from time import sleep
from discord.ext import commands


## Whitelisted Servers 
whitelistedServers=[1286147910085513287]



class tourn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(tourn(bot))