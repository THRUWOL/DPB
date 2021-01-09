import discord

from discord.ext import commands
from discord import Member, Guild

import secret.token as token

client = commands.Bot(command_prefix='.')

extensions = [
    'secret.db',
    'commands.main'
]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


print("bot.py started")
client.run(token.TOKEN)