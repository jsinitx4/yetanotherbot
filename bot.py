import discord
import asyncio
import youtube_dl
import random

from discord.ext import commands
from assets.list import *
prefix = "$"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

extensions = [
    "commands.useful_stuff"
    ]

if __name__ ==  '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print("loaded {}".format(extension))
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extensions, error))


players = {}

@bot.event
async def on_ready():
    print("successful startup")
    await bot.change_presence(game=discord.Game(name='fortnite 2'))


@bot.command(pass_context=True)
async def say(ctx, *, content:str):
    await ctx.send(content)

@bot.command(name="8ball")
async def ball(ctx):
    okbuddy = random.choice(differentball)
    await ctx.send(okbuddy)

@bot.command(pass_context=True)
async def dev(ctx): #this was all a mistake
    await ctx.send("my daddy is `speed#5496`")

@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command(pass_context=True)
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)

@bot.command(pass_context=True)
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)

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
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await ctx.send("ok")

@commands.command(pass_context=True)
async def play( ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@bot.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await ctx.send("hi welcome back")

@bot.command(pass_context=True)
async def math(ctx): 
    await ctx.send("`subcommands` $add, $divide, $subtract, $multiply")

@bot.command(pass_context=True)
async def invite(ctx): 
    await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=490953980361441281&permissions=8&scope=bot")

@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="help", description="thank you pylint, very cool!", color=0x00FFDD)
    embed.add_field(name="useful stuff", value="`$say, $dev, $math, $8ball, $invite`", inline= True)
    embed.add_field(name="useless stuff", value="`nothing useless yet`", inline= True)
    embed.add_field(name="music", value="`$join, $leave, $play, $pause, $leave`")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def load(extension):
    try:
        bot.load_extension(extension)
        print("loaded {}".format(extension))
    except Exception as error:
        print("failed to load extension {} [{}]".format(extensions, error))

@bot.command(pass_context=True)
async def unload(extensions):
    try:
        bot.unload_extension(extension)
        print("unloaded {}".format(extension))
    except Exception as error:
        print("failed to unload extension {} [{}]".format(extensions, error))

bot.run("TOKEN")