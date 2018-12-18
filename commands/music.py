import discord
import asyncio
import youtube_dl

from discord.ext import commands 

class music:
    def __init__(self, bot):
        self.bot = bot 

players = {}

@commands.command()
async def play(self, ctx, url):
    server = ctx.message.server
    voice_client = self.bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@commands.command()
async def join(self, ctx):
    channel = ctx.message.author.voice.voice_channel
    await self.bot.join_voice_channel(channel)

@commands.command()
async def leave(self, ctx):
    server = ctx.message.server
    voice_client = self.bot.voice_client_in(server)
    await voice_client.disconnect()

@commands.command()
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
    await ctx.send("ok")

@commands.command()
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
    await ctx.send("hi welcome back")

def setup(bot):
    bot.add_cog(music(bot))