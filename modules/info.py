import discord
from discord.ext import commands
import datetime
import time
import subprocess
import traceback
import requests
import random
from random import choice as rnd
from random import choice, randint
import aiohttp
import asyncio
import sys
import json
import config

class Info:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['mice'])
    async def mouse(self, ctx, username:str=None):
        if not username:
            await ctx.send('Please add the username. Example: `s;mouse Glaatt` or `s;mouse Glaatt#0000`')
        rounds = 0
        gathered_cheese = 0
        shaman_cheese = 0
        saved_mice = 0
        saved_mice_hard = 0
        saved_mice_divine = 0
        completed_bootcamp = 0
        shaman_colour = None
        firsts = 0
        exp = 0
        level = 0
        
        embed = discord.Embed(colour=0x009d9d)
        embed.description = f''
        embed.add_field(name='Gathered Cheese', value=f'<:Cheese:526136841620029450> {gathered_cheese}')
        embed.add_field(name='Firsts', value=f'<:Mouse:526136041774514198> {firsts}')
        embed.add_field(name='Rounds Played', value=f'<:arrow:526138664515010562>{rounds}')
        embed.add_field(name='Bootcamp', value=f'<:bootcamp:526135198929387530> {completed_bootcamp}')
        embed.add_field(name="Saved Mice", value=f'<:shamanNormal:526131454078353409>{saved_mice}<:shamanHard:526132068179116033>{saved_mice_hard}<:shamanDivine:526132090740277289>{saved_mice_divine}')
        embed.set_author(name=username.capitalize(), icon_url='https://vignette.wikia.nocookie.net/transformice/images/3/3a/Chatmane.png/revision/latest?cb=20160205093856')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/491039615185059850/525098215544979481/image0.jpg?width=440&height=434')
        await ctx.send(embed=embed)
        


def setup(bot):
  bot.add_cog(Info(bot))
