import asyncio
import os
from dotenv import load_dotenv
from rust.socket import create_socket
from rust.chat import watch_team_chat
from bot.client import create_client

load_dotenv()

async def main():
    socket = await create_socket()

    asyncio.create_task(watch_team_chat(socket))

    client = create_client(socket)
    await client.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())