import disnake
from disnake.ext import commands

class OwnerOnly(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.author.id == 181064730075463680

    async def send_no_permission_message(self, ctx, message: str, image_url: str):
        embed = disnake.Embed(
            title="No Permission",
            description=message,
            color=disnake.Color.red()
        )
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx, status_type: str):
        status_dict = {
            'online': disnake.Status.online,
            'idle': disnake.Status.idle,
            'invisible': disnake.Status.invisible,
            'dnd': disnake.Status.dnd
        }
        if status_type.lower() in status_dict:
            await self.bot.change_presence(status=status_dict[status_type.lower()])
            await ctx.send(f"Status changed to {status_type}")
        else:
            await ctx.send("Invalid status type. Choose from: 'online', 'idle', 'invisible', 'dnd'.")

    @commands.command()
    async def playing(self, ctx, *, activity: str):
        await self.bot.change_presence(activity=disnake.Game(name=activity))
        await ctx.send(f"Now playing: {activity}")

    @commands.command()
    async def listening(self, ctx, *, activity: str):
        await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name=activity))
        await ctx.send(f"Now listening to: {activity}")

    @commands.command()
    async def watching(self, ctx, *, activity: str):
        await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=activity))
        await ctx.send(f"Now watching: {activity}")

    @commands.command()
    async def streaming(self, ctx, *, url: str):
        await self.bot.change_presence(activity=disnake.Streaming(name="Streaming now", url=url))
        await ctx.send(f"Now streaming: {url}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await self.send_no_permission_message(
                ctx,
                "You do not have permission to use this command.",
                "https://media.discordapp.net/attachments/1274184520765018122/1279035344955637821/Flag_of_Vietnam.png?ex=66d2f9fd&is=66d1a87d&hm=155f231ad87553eae7dc28484bd5f2da10763dcc31419b80d3c51a3f96420cef&=&format=webp&quality=lossless&width=702&height=468"
            )
        else:
            # Nếu có lỗi khác, bạn có thể xử lý ở đây hoặc bỏ qua
            pass

def setup(bot):
    bot.add_cog(OwnerOnly(bot))
