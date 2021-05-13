import discord
from discord.ext import commands
import json
import os

client = commands.Bot(command_prefix="!")
client.remove_command("help")

os.chdir(r'/Users/jangi/Desktop/Discord Bot')

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="CONAN-BOT",
        description="Commands",
        color=discord.Color.blue(),
        author="A"
    )
    embed.set_thumbnail(url="http://localhost/programs/bot_logo.png")
    embed.add_field(name="!help", value="List all commands", inline=True)
    embed.add_field(name="!ping", value="Reply with 'pong!'", inline=True)
    
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

with open('data/token.json', 'r') as f:
    token = json.load(f)

client.run(token["TOKEN"])

with open('data/token.json', 'r') as f:
    json.dump(token, f)