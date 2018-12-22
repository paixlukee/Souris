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

class Developer:
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command(aliases=['debug', 'ev'])
    @commands.is_owner()
    async def eval(self, ctx, *, code):
        o_code = code
        code = code.replace('“', '"').replace('”', '"').replace("-silent", "").replace("-s", "").replace("```py", "").replace("```", "")
        try:
            env = {
                'bot': ctx.bot,
                'ctx': ctx,
                'channel': ctx.message.channel,
                'author': ctx.message.author,
                'guild': ctx.message.guild,
                'message': ctx.message,
                'discord': discord,
                'random': random,
                'commands': commands,
                'requests': requests,
                'asyncio': asyncio,
                're': re,
                'os': os,
                'db': db,
                'rnd': rnd,
                '_': self._last_result
            }
            try:
                result = eval(code, env)
            except SyntaxError as e:
                await ctx.send(f'```py\n{e}```')
            except Exception as e:
                await ctx.send(f'```py\n{e}```')
            if asyncio.iscoroutine(result):
                result = await result
            self._last_result = result            
            if code == "bot.http.token":
                await ctx.send(f'```Token blocked.```')
            
            elif o_code.endswith(" -silent") or o_code.endswith(" -s"):
                pass
            
            else:
                if len(str(result)) > 1500:
                    r = requests.post(f"https://hastebin.com/documents", data=str(result).encode('utf-8')).json()
                    return await ctx.send(f'https://hastebin.com/' + r['key'])                    
                else:
                    try:
                        await ctx.send(f'```py\n{result}```')
                    except Exception as e:
                        await ctx.send(f'```py\n{e}```')
        except Exception as e:
            await ctx.send(f'```py\n{e}```')
            

def setup(bot):
  bot.add_cog(Developer(bot))
