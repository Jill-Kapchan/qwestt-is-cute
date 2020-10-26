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
                aliases=['simpforme', 'simp'],
                pass_context=True)
async def simpForMe(context):
    possible_responses = [
        'Call me old fashioned but I was born and raised to serve ' + context.message.author.mention + '. I was destined to cook for them, bathe them, do their laundry, and wash their dishes. I only live to cater to their needs. I am their property and if they ever cheats on me thats my fault and they caught me slipping',
        'Daddy ' + context.message.author.mention,
        context.message.author.mention + ' senpai',
        context.message.author.mention + ' oppa',
        "I'll be the e-girl to your e-" + context.message.author.mention + "<3",
        context.message.author.mention + ' u so icy Ima glacier boy',
        'Degrade me ' + context.message.author.mention
    ]
    await client.say(random.choice(possible_responses))


@client.command(name='simpForQwestt',
                aliases=['simpforqwestt', 'simpforQwestt', 'simpForqwestt'],
                pass_context=True)
async def simpForMe(context):
    qwestt = 'Call me old fashioned but I was born and raised to serve Qwestt. I was destined to cook for him, bathe him, do his laundry, and wash his dishes. I only live to cater to his needs. I am his property and if he ever cheats on me thats my fault and he caught me slipping.'
    await client.say(qwestt)


@client.command(name='stan',
                aliases=['Stan', 'STAN'],
                pass_context=True)
async def stan(context):
    possible_responses = [
        'STAN LOONA',
        'STAN Stray Kids',
        'STAN NCT',
        'STAN ATEEZ',
        'STAN Twice',
        'STAN BTS',
    ]
    await client.say(random.choice(possible_responses) + " " + context.message.author.mention)


@client.command(name='ship',
                aliases=['gaymers', 'Ship'],
                pass_context=True)
async def stan(context):
    possible_responses = [
        'Qwestt',
        'Scott',
        'Wilson',
        'Donovan',
        'Nick',
        'Ryan',
        'Brian',
        'Erik'
    ]
    choice = random.sample(possible_responses, 2)
    await client.say(choice[0] + " x " + choice[1])


@client.command(name='loona',
                aliases=['Loona', 'LOONA'],
                pass_context=True)
async def stan(context):
    loon = 'Loona (stylized as LOOΠΔ, Korean: 이달의 소녀; Hanja: 이달의 少女; RR: Idarui Sonyeo; lit. '"Girl of the Month"') is a South Korean girl group formed by Blockberry Creative. The group was introduced to the public through a pre-debut project which began in October 2016, where each of the twelve members were revealed in a periodic fashion by releasing a promotional single over the following eighteen months. They debuted as a full ensemble with the extended play, [+ +] (2018), supported by the lead single "Favorite" and the title track "Hi High."'
    insta ='\nInstagram: https://www.instagram.com/loonatheworld/'
    youtube='\nYoutube: https://www.youtube.com/c/loonatheworld/featured'
    twitter ='\nTwitter: https://twitter.com/loonatheworld'
    shop = '\nShop: https://shop.loonatheworldus.com/'
    await client.say(loon + insta + youtube + twitter + shop)


@client.event
async def on_message(message):
    if message.content.startswith('!del'):
        await asyncio.sleep(1)
        await message.channel.purge(limit=1)
        #await client.delete_message(message)

@client.event
async def on_message(message):
    if message.content.startswith('!d'):
        await asyncio.sleep(1)
        await client.delete_message(message)


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