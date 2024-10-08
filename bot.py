import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os

# Load token từ file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Định nghĩa intents
intents = disnake.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned,
    intents=intents,
    help_command=commands.DefaultHelpCommand(),
)

# Sự kiện khi bot đã sẵn sàng
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# Load các cogs
for folder in os.listdir('./cogs'):
    for filename in os.listdir(f'./cogs/{folder}'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{folder}.{filename[:-3]}')


# Chạy bot
bot.run(TOKEN)
