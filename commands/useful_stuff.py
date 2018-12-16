import discord
import asyncio
import youtube_dl
import random

from discord.ext import commands 
from assets.list import *

class useful_stuff:
    def __init__(self, bot):
        self.bot = bot 

@commands.command(name="8ball")
async def ball(self, ctx):
    okbuddy = random.choice(differentball)
    await ctx.send(okbuddy)

@commands.command(pass_context=True)
async def math(self, ctx): 
    await ctx.send("`subcommands` $add, $divide, $subtract, $multiply")

@commands.command(pass_context=True)
async def add(self, ctx, a: int, b: int):
    await ctx.send(a + b)

@commands.command(pass_context=True)
async def dev(self, ctx): #this was all a mistake
    await ctx.send("my daddy is `speed#5496`")

@commands.command(pass_context=True)
async def multiply(self, ctx, a: int, b: int):
    await ctx.send(a * b)

@commands.command(pass_context=True)
async def subtract(self, ctx, a: int, b: int):
    await ctx.send(a - b)

@commands.command(pass_context=True)
async def divide(self, ctx, a: int, b: int):
    await ctx.send(a / b)


def setup(bot):
    bot.add_cog(useful_stuff(bot))