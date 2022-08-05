import discord
from discord.ext import commands
from config import settings
import json
import requests
import random
import time
from discord import FFmpegPCMAudio
import os


reactions = ['Какой красивый ,не то что ты','Мимими,не то что ты','Даже он лучше на миду стоит','Это разраб кста',]

bot = commands.Bot(command_prefix = settings['prefix'],intents= discord.Intents.all())
@bot.event
async def on_ready( ):
           print("Bot gotov 1x1 on mid")


@bot.command() 
async def hello(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Go lobby, {author.mention}!') 

@bot.command() 
async def go(ctx): 
    author = ctx.message.author 
    await ctx.send(f'ti debil ya bot, {author.mention}!') 

@bot.command()
async def red_panda(ctx):

    response = requests.get('https://some-random-api.ml/img/red_panda') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xDC143C, title = random.choice(reactions)) 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def hug(ctx):
    response = requests.get('https://some-random-api.ml/animu/hug') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xDC143C, title = 'Это я кста')
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def ghul(ctx):
	b = 1000
	while b>0:
		time.sleep(0.5)
		await ctx.send(f'1000-7 = {b}')
		b -=7

@bot.command()
async def author(ctx):
	await ctx.send(f'https://github.com/piSINUS Это я кста создал це чудище да да я ')

@bot.command()
async def pat(ctx):
    response = requests.get('https://some-random-api.ml/animu/pat') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xDC143C, title = 'Это моя кста')
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def флирт (ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xDC143C, title = 'Го ыбатся')
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 


bot.run(settings['token']) 