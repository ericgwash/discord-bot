import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
@client.event
async def on_ready():
    print(f'{client.user.name} has joined Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello {member.name}!! Welcome to Our Discord Server!'
    )        
keep_alive()
client.run("INSERT TOKEN ID HERE ")
