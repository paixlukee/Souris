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


def setup(bot):
  bot.add_cog(Help(bot))