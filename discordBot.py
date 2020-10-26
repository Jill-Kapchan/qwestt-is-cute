# Work with Python 3.6
import os
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='simpForMe',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['simpforme', 'simp'],
                pass_context=True)
async def simpForMe(context):
    possible_responses = [
        'Call me old fashioned but I was born and raised to serve'+ context.message.author.mention + '. I was destined to cook for them, bathe them, do their laundry, and wash their dishes. I only live to cater to their needs. I am their property and if they ever cheats on me thats my fault and they caught me slipping',
        'Daddy',
        'Senpai',
        'Oppa',
        "I'll be the e-girl to your e-" + context.message.author.mention + "<3",
        'u so icy Ima glacier boy',
        'Degrade me'
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="simping for Qwestt"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

client.run(os.getenv('BOT_TOKEN'))