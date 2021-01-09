import discord
import asyncio
import sqlite3
import os

from discord.ext import commands
from discord import Member, Guild

sql = sqlite3.connect('server.db')
cursor = sql.cursor()

class all_commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.has_permissions(view_audit_log = True)
    async def clear(self,ctx,amount = 0,reason = None):
        await ctx.channel.purge(limit = amount + 1)
        if amount > 0:
            if reason is None:
                await ctx.send(embed = discord.Embed(
                color = 0x3caa3c, #green
                title = ".clear",
                description = f"""Пользователь **{ctx.author}** безпричинно избавил этот мир от **{amount}** сообщений"""
                ))
            else:
                await ctx.send(embed = discord.Embed(
                color = 0x3caa3c,
                title = ".clear",
                description = f"""Пользователь **{ctx.author}** утилизировал **{amount}** сообщений по причине {reason}"""
                ))
        elif amount == 0 or amount < 0: 
            await ctx.send(embed = discord.Embed(
            color = 0x3caa3c,
            title = ".clear",
            description = f"""Пользователь **{ctx.author}** ничего не сделал, но всем понравилось"""))

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = ".help"))

    @commands.Cog.listener("on_message")
    async def parrot(self,message):
        channel = self.bot.get_channel(796677661577314379) #канал, куда улетают дублированные сообщения
        if message.author.bot:  #не дублирует сообщения от бота (иначе будет рекурсия)
            pass
        else:  #если сообщение не от бота, то оно дублируется ботом
            await channel.send(message.content)
def setup(bot):
    print("main started")
    bot.add_cog(all_commands(bot))