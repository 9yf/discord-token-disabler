
from discord.ext import commands
import discord
import requests
import random
import time
import threading
import asyncio

bot = commands.Bot(self_bot=True, command_prefix="$")

token = input("Token: ")




headers = {'Authorization': f"{token}"}
number = random.randint(666, 69420)

def massban(guild, members):
    while True:
        for member in members:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    break
                else:
                    break

@bot.event
async def on_ready():
    g = await bot.create_guild(name=number)
    members = open('ids.txt')
    for i in range(20):
        t = threading.Thread(target=massban, args=(g.id, members,))
        t.start()






bot.run(token, bot=False)
