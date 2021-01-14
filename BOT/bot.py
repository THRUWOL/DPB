import discord

from discord.ext import commands
from discord import Member, Guild

import secret.settings as settings

client = commands.Bot(command_prefix='.')

extensions = [
    'secret.db',
    'commands.main',
    'games.minesweeper'
]

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


print("bot.py started")
client.run(settings.TOKEN)