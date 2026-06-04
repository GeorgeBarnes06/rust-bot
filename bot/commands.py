import discord
from discord import app_commands

def setup_commands(tree: app_commands.CommandTree, socket, config):

    @tree.command(name="info", description="Get server info")
    async def info(interaction: discord.Interaction):
        await interaction.response.defer()
        server_info = await socket.get_info()
        time = await socket.get_time()

        embed = discord.Embed(
            title="Server Information",
            color=discord.Color.green()
        )

        embed.add_field(name="Players", value=f"{server_info.players}/{server_info.max_players}", inline=True)
        embed.add_field(name="Time", value=time.time, inline=True)
        embed.add_field(name="Wipe", value="Unknown", inline=True)
        embed.set_footer(text=server_info.name)

        await interaction.followup.send(embed=embed)  # indented inside the function

    @tree.command(name="team", description="Get team status")
    async def team(interaction: discord.Interaction):
        pass

    @tree.command(name="time", description="Get in-game time")
    async def time_cmd(interaction: discord.Interaction):
        pass

    @tree.command(name="players", description="Get player count")
    async def players(interaction: discord.Interaction):
        pass