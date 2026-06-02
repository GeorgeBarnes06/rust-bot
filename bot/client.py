import json
import discord
from discord import app_commands
from bot.commands import setup_commands

def create_client(socket):
    with open("config.json") as f:
        config = json.load(f)

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    setup_commands(tree, socket, config)

    @client.event
    async def on_ready():
        print(f"Discord bot logged in as {client.user}")
        await tree.sync()
        print("Slash commands synced!")

    return client