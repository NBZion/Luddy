import discord
import json
from time import sleep
from discord.ext import commands


## Whitelisted Servers 
whitelistedServers=[1286147910085513287]



class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command(guild_ids=whitelistedServers, description="Deletes messages")
    @commands.has_permissions(ban_members=True)
    async def purge(self, ctx, amount: int):
        messages = await ctx.channel.history(limit=amount).flatten()
        for message in messages:
            await message.delete()

        await ctx.respond("Deleted messages",ephemeral = True)
        deleteMsg = await ctx.send(f"Deleted {amount} messages")
        sleep(5)
        await deleteMsg.delete()



def setup(bot):
    bot.add_cog(mod(bot))