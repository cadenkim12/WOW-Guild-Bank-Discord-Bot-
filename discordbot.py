from dotenv import load_dotenv
import os
import discord
load_dotenv()

from RawMats import RawMats
from cmds import cmds

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()

    if content.startswith("/get"):
        response = cmds.get(content)
        await message.channel.send(response)

    elif content.startswith("/help"):
        response = cmds.help(content)
        if response:
            await message.channel.send(response)

    elif content.startswith("/refresh"):
        RawMats.refresh()
        await message.channel.send("Guild bank data refreshed.")


client.run(TOKEN)