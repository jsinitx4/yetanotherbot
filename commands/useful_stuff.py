import random

from discord.ext import commands 
from assets.list import *

class useful_stuff:
    def __init__(self, bot):
        self.bot = bot 

@commands.command()
async def say(ctx, *, content:str):
    await ctx.send(content)

@commands.command(name="8ball")
async def ball(ctx):
    okbuddy = random.choice(differentball)
    await ctx.send(okbuddy)

@commands.command()
async def invite(ctx): 
    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=490953980361441281&permissions=8&scope=bot")

@commands.command()
async def math(ctx): 
    await ctx.send("`subcommands` $add, $divide, $subtract, $multiply")

@commands.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@commands.command()
async def dev(ctx): #this was all a mistake
    await ctx.send("my daddy is `speed#5496`")

@commands.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@commands.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)

@commands.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)


def setup(bot):
    bot.add_cog(useful_stuff(bot))
