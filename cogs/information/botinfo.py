import platform
import time
from datetime import timedelta
import disnake
from disnake.ext import commands

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @commands.command()
    async def botinfo(self, ctx):
        # Tính toán uptime
        current_time = time.time()
        uptime_seconds = int(current_time - self.start_time)
        uptime_str = str(timedelta(seconds=uptime_seconds))

        # Lấy thông tin phiên bản
        python_version = platform.python_version()
        disnake_version = disnake.__version__
        os_version = platform.system() + " " + platform.release()

        # Lấy số lượng máy chủ, người dùng và bot
        total_guilds = len(self.bot.guilds)
        total_users = sum(len(guild.members) for guild in self.bot.guilds)
        total_bots = sum(1 for guild in self.bot.guilds for member in guild.members if member.bot)
        total_humans = total_users - total_bots

        # Tạo embed để hiển thị thông tin
        embed = disnake.Embed(title="Bot Information", color=disnake.Color.blurple())
        embed.add_field(name="Servers", value=total_guilds, inline=True)
        embed.add_field(name="Users", value=total_users, inline=True)
        embed.add_field(name="Bots", value=total_bots, inline=True)
        embed.add_field(name="Humans", value=total_humans, inline=True)
        embed.add_field(name="Uptime", value=uptime_str, inline=False)
        embed.add_field(name="Python Version", value=python_version, inline=True)
        embed.add_field(name="Disnake Version", value=disnake_version, inline=True)
        embed.add_field(name="OS Version", value=os_version, inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        # Tính toán độ trễ API
        start_time = time.time()
        message = await ctx.send("Pinging...")
        end_time = time.time()
        api_latency = round((end_time - start_time) * 1000)  # Độ trễ API tính bằng ms

        # Độ trễ websocket
        websocket_latency = round(self.bot.latency * 1000)  # Độ trễ websocket tính bằng ms

        # Cập nhật thông tin trong embed
        embed = disnake.Embed(title="Pong! 🏓", color=disnake.Color.green())
        embed.add_field(name="API Latency", value=f"{api_latency} ms")
        embed.add_field(name="WebSocket Latency", value=f"{websocket_latency} ms")

        await message.edit(content=None, embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
