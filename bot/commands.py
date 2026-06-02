import discord
from discord import app_commands

def setup_commands(tree: app_commands.CommandTree, socket, config):

    @tree.command(name="info", description="Get server info")
    async def info(interaction: discord.Interaction):
        await interaction.response.defer()
        server_info = await socket.get_info()
        time = await socket.get_time()
        await interaction.followup.send(
            f"🟢 **{server_info.name}**\n"
            f"👥 Players: {server_info.players}/{server_info.max_players}\n"
            f"🕐 Time: {time.time}"
        )

    @tree.command(name="team", description="Get team status")
    async def team(interaction: discord.Interaction):
        pass

    @tree.command(name="time", description="Get in-game time")
    async def time_cmd(interaction: discord.Interaction):
        pass

    @tree.command(name="players", description="Get player count")
    async def players(interaction: discord.Interaction):
        pass