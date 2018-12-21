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

extensions = ['modules.info']

class Souris(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix='s;')
        self.remove_command("help")
        self.add_command(self.ping)
        
    async def on_message_edit(self, before, after):
        if not self.is_ready() or after.author.bot:
            return

        await self.process_commands(after)#hi thanks

    async def status_task(self):
        users = len(set(self.get_all_members()))
        sayings = [f'{users} users', f'{str(len(self.guilds))} guilds']
        while True:
            game = discord.Activity(name=f'{rnd(sayings)} | s;help', type=discord.ActivityType.watching)
            await self.change_presence(status=discord.Status.online, activity=game)
            await asyncio.sleep(30)

    async def on_ready(self):
        print('\n------')
        print(f'[UPDATE] Logged in as: {self.user.name]')
        print(f"[AWAITING] Run 's;load all'")
        print("\n------\n\n")
        self.loop.create_task(self.status_task())

    async def on_guild_join(self, guild):
        targs = [
            discord.utils.get(server.channels, name="bot"),
            discord.utils.get(server.channels, name="bots"),
            discord.utils.get(server.channels, name="bot-commands"),
            discord.utils.get(server.channels, name="bot-spam"),
            discord.utils.get(server.channels, name="bot-channel"),
            discord.utils.get(server.channels, name="testing"),
            discord.utils.get(server.channels, name="testing-1"),
            discord.utils.get(server.channels, name="general"),
            discord.utils.get(server.channels, name="shitposts"),
            guild.get_member(guild.owner.id)
            ]
        for x in targs:
            try:
                await x.send(":mouse::wave: Hello! I am **Souris**! Thank you for inviting me to your guild! For help with my commands, send `s;help`.")
            except:
                continue
            break

    @commands.command()
    async def ping(self, ctx):
        """useless command"""
        await ctx.send("Pong! Have a mice day!")
                                        
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        try:
            if extension == 'all':
                for extension in extensions:
                    not_loaded = []
                    loaded = []
                    try:
                        self.load_extension(extension)
                        loaded.append(extension)
                    except Exception as error:
                        print('\n\nMODULE ERROR: {} was not loaded due to an error: \n-- [{}] --\n\n'.format(extension, error))
                        not_loaded.append(f'{extension} ({error})')
                nl_list = ", ".join(not_loaded)
                l_list = "\n**Not Loaded**: " + ", ".join(loaded)
                await ctx.send(f'**Loaded**: {l_list}{nl_list}')
            else:
                self.load_extension("modules.{}".format(extension))
                self.load_extension(extension)
                await ctx.send('Module has been loaded.')
                print('\n\nMODULE LOAD\n--[Module loaded, {}.py]--\n\n'.format(extension))
        except Exception as error:
            print('\n\nMODULE ERROR: {} was not loaded due to an error: \n-- [{}] --\n\n'.format(extension, error))
            await ctx.send(f'Could not load module: `{error}`')

    @commands.command(aliases=['un'], hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.unload_extension("modules.{}".format(extension))
        await ctx.send('Module has been loaded.')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You do not meet the correct permissions to run this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"Incorrect Argument(s): `{error}`")
        elif isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(error.retry_after, 60)
            hours, minutes = divmod(minutes, 60)
            if hours >= 1:
                hours = f"{round(hours)}h"
            else:
                hours = ""
            await ctx.send(":alarm_clock: Please wait **{hours} {round(minutes)}m {round(seconds)}s** before using this command again.")
        else:
            print(f"[{type(error).__name__.upper()}]: {error}")

    async def on_message(self, message):
        if message.author.bot: return
        await self.process_commands(message)
        
    def run(self):
        super().run(config.token, reconnect=True)
