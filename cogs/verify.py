import gspread
from discord.ext import commands
from discord.commands import Option

## Whitelisted Servers 
whitelistedServers=[1286147910085513287]

gc = gspread.service_account(filename='credentials.json')

commiteeList = gc.open_by_url("https://docs.google.com/spreadsheets/d/1tyt7ahVJ883nUckPmxivP8DujdjlHVmSJviXZp-3_h4/edit?usp=sharing")
memberList = gc.open_by_url("https://docs.google.com/spreadsheets/d/1b6fxvTrmCV6Z3C9pa1zN7slG5-Ss6Tj2dP8c2T71dCw/edit?usp=sharing")

class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.respond(f"Welcome to the Official LUDO discord server {member.mention}, Please make sure to verify by looking at <#1286179185622126642>!")

    @commands.slash_command(guild_ids=whitelistedServers, description="Sends the bot's latency")
    async def ping(self, ctx):
        await ctx.respond(f"Pong! {round(self.bot.latency)*100}ms")

    @commands.slash_command(guild_ids=whitelistedServers, description="Lists commitee members listed in the form")
    @commands.has_permissions(manage_messages=True)
    async def list_committee(self, ctx):
        comMember = commiteeList.sheet1.col_values(1)
        comMember.pop(0)

        await ctx.respond("```" + ",\n ".join(comMember) + "```")

    @commands.slash_command(guild_ids=whitelistedServers, description="Verifies your account to be let in the server")
    async def verify(self, ctx, idnum: int, email: str,committeedec:Option(str,"Pick YES or NO",choices=["YES","NO"],default="NO")):
        comEmailList = commiteeList.sheet1.col_values(2)
        idMemList =  memberList.sheet1.col_values(7)
        idMemList.pop(0)
        comEmailList.pop(0)

        if committeedec == "NO":
            if str(idnum) in idMemList:
                ctx.author.add_roles(ctx.guild.get_role(1286149007172702264))
                await ctx.respond("Succesfully Verified! Welcome to LUDO!",ephemeral = True)
            #    await ctx.respond("Server is still closed to Regular Members!")

            else:
                await ctx.respond("Verification Failed, Please Contact LUDO Committee!",ephemeral = True)
            #    await ctx.respond("Server is still closed to Regular Members!")
        elif committeedec == "YES":
            if email in comEmailList:
                ctx.author.add_roles(ctx.guild.get_role(1286149007172702264))
                ctx.author.add_roles(ctx.guild.get_role(1286148423954726912))
                await ctx.respond("Welcome Committee! Happy to see you Here! Please make your introduction at <#1288662343890501663> so we can get to know each other!",ephemeral = True)
            else:
                await ctx.respond("Email Not Detected in List, Please Contact Committee!",ephemeral = True)
        



def setup(bot):
    bot.add_cog(verify(bot))