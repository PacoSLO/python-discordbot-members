from discord.ext import commands
import discord

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

    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 0    # I've added a '-1' because guild.member_count includes all users and bots including your own bot
    
    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{members} Members'
    ))

#BOT TOKEN
bot.run('YOUR TOKEN HERE')

