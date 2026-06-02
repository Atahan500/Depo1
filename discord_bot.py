import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("MTQyOTg0OTYzNDk4MTAyMzg1NQ.GjpB2S.xucgWn8BBzEthnk1nAEQVYY8u3pgtQe84IZtFE")