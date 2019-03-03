import discord
import asyncio
import youtube_dl
import random

import sys, traceback

from discord.ext import commands
from assets.list import *
prefix = "$"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

players = {}

@bot.event
async def on_ready():
    print("successful startup")
    await bot.change_presence(game=discord.Game(name='fortnite 2'))

@bot.command(pass_context=True)
async def say(ctx, *, content:str):
    await bot.say(content)

@bot.command(name="8ball")
async def ball(ctx):
    okbuddy = random.choice(differentball)
    await bot.say(okbuddy)

@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
    await bot.say(a + b)

@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    await bot.say(a * b)

@bot.command(pass_context=True)
async def subtract(ctx, a: int, b: int):
    await bot.say(a - b)

@bot.command(pass_context=True)
async def divide(ctx, a: int, b: int):
    await bot.say(a / b)

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    await bot.say("now playing")

@bot.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await bot.say("ok")

@bot.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await bot.say("hi welcome back")

@bot.command(pass_context=True)
async def math(ctx): 
    await bot.say("`subcommands` $add, $divide, $subtract, $multiply")

@bot.command(pass_context=True)
async def invite(ctx): 
    await bot.say("https://discordapp.com/api/oauth2/authorize?client_id=490953980361441281&permissions=8&scope=bot")

@bot.command(pass_context=True)
async def dev(ctx): 
    await bot.say("`speed#3413`")

@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="help", description="thank you pylint, very cool!", color=0x00FFDD)
    embed.add_field(name="useful stuff", value="`$say, $dev, $math, $8ball, $invite`", inline= True)
    embed.add_field(name="useless stuff", value="`nothing useless yet`", inline= True)
    embed.add_field(name="music", value="`$join, $leave, $play, $pause, $resume`")
    await bot.say(embed=embed)
            
bot.run("TOKEN")
