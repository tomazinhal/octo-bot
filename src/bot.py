import discord
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse  import urlencode
import json

TOKEN = 'MzM5NTUwOTc5Mzk1NDIwMTcx.DF_rkQ.GVPIU-ouYQHUToX_lKVzYuV4AjI'

description = '''octo-bot in Python'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def gif(tag=''):
    """Search for gif"""
    query = 'https://api.giphy.com/v1/gifs/random?'
    params = urlencode({
        'api_key': '62b0f8d737c7419ba2620fcfb6b02a12',
        'tag': tag,
        'rating': 'G' # [Y, G, PG, PG-13, R]
        })
    res = json.loads(urlopen(query+params).read())
    img = 'https://i.giphy.com/' + res['data']['id'] + '.gif'
    await bot.say(img)

bot.run(TOKEN)