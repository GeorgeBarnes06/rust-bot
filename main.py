import asyncio
import os
import json
import discord
from rustplus import RustSocket, ServerDetails
from dotenv import load_dotenv

load_dotenv()

async def main():
    with open("config.json") as f:
        config = json.load(f)

    # Set up Discord client
    intents = discord.Intents.default()
    discord_client = discord.Client(intents=intents)

    r = config["rust"]
    details = ServerDetails(r["ip"], r["port"], r["steam_id"], r["player_token"])
    socket = RustSocket(details)

    @discord_client.event
    async def on_ready():
        print(f"Discord bot logged in as {discord_client.user}")

        # Connect to Rust
        await socket.connect()

        info = await socket.get_info()
        time = await socket.get_time()

        # Send message to Discord channel
        channel = discord_client.get_channel(int(config["channels"]["main"]))
        await channel.send(
            f"🟢 **{info.name}**\n"
            f"👥 Players: {info.players}/{info.max_players}\n"
            f"🕐 Time: {time.time}"
        )

        await socket.disconnect()
        await discord_client.close()

    await discord_client.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())