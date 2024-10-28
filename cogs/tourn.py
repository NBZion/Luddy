import discord
import json
from time import sleep
from discord.ext import commands


## Whitelisted Servers 
whitelistedServers=[1286147910085513287]



class tourn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(guild_ids=whitelistedServers, description="Adds a Team for Ludopocalypse")
    @commands.has_permissions(manage_messages=True)
    async def add_team(ctx, teamName):
        guild = ctx.guild()

        organizerRole = ctx.guild.get_role()

        teamRole = await guild.create_role(name=teamName)

        team_category = await guild.create_category("TEAM | " + teamName)

        await guild.create_text_channel(f"{teamName}-text", category=team_category)
        await guild.create_voice_channel(f"{teamName}-voice", category=team_category)

        # Set everyone to not see VC
        await team_category.set_permissions(guild.default_role, view_channel=False)

        await team_category.set_permissions(teamRole, view_channel=True, send_messages=True, connect=True)
        await team_category.set_permissions(organizerRole, view_channel=True, send_messages=True, connect=True)

        await ctx.respond("Succesfully created team '" + teamName + "'!") 



def setup(bot):
    bot.add_cog(tourn(bot))