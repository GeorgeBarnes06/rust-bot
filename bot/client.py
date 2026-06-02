import json
import discord

def create_client(socket):
    with open("config.json") as f:
        config = json.load(f)

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"Discord bot logged in as {client.user}")

        info = await socket.get_info()
        time = await socket.get_time()
        team = await socket.get_team_info()

        # Print team members
        for member in team.members:
            print(member.name)

        # Send to Discord
        channel = client.get_channel(int(config["channels"]["main"]))
        await channel.send(
            f"🟢 **{info.name}**\n"
            f"👥 Players: {info.players}/{info.max_players}\n"
            f"🕐 Time: {time.time}"
        )

    return client