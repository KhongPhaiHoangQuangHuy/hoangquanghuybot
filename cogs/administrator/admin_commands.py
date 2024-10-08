import disnake
from disnake.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mgs(self, ctx, channel: disnake.TextChannel, *, content: str):
        """"""
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("You do not have permission to use this command.")
            return

        try:
            await channel.send(content)
            await ctx.send(f"Message sent to {channel.mention}")
        except disnake.Forbidden:
            await ctx.send("I do not have permission to send messages to that channel.")

def setup(bot):
    bot.add_cog(AdminCommands(bot))
