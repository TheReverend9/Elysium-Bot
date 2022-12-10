#!/usr/bin/env python

'''
Created: 12/10/2022

Author: Kevin Blackmon
Company: Reverend Studios
'''

import discord
import asyncio
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
landingChannel = os.getenv("landing_station")



@client.event
async def on_member_join(member):
    channel = client.get_channel(int(landingChannel))
    with open('newMemberMsg.txt') as file:
        newMemberMsg = file.read()
    await channel.send(newMemberMsg)

client.run(TOKEN)