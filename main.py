from discord.ext import tasks, commands
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext.commands import Context

# Just add your desired prefix there.
bot = commands.Bot(command_prefix='!')

#Bot status
@bot.event
async def on_ready():  # This function is run upon the bots startup completing
    # os.system('cls')
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Status: Running")
    print("########################################")

#REFREST STATUS MSG
@tasks.loop(seconds=18000)
async def status_task() -> None:
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 0
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f'{members} Members'))
    await asyncio.sleep(18000)

#BOT TOKEN
bot.run('YOUR TOKEN HERE')
