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

class Help:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['cmds', 'Help'])
    async def help(self, ctx):
        helpd = '`mouse <username>` - Get information about a specific mouse\n'\
                '`tribe <name>` - Get information about a specific tribe'#\
                #'`` -'\
                #''\
                #''\
                #''\
        embed = discord.Embed(colour=0x009d9d, description=helpd)
        embed.set_footer(text='Arguments are represented as <>')
        await ctx.send(embed=embed, content=':mouse: Here is a list of my commands!')
    


def setup(bot):
  bot.add_cog(Help(bot))
