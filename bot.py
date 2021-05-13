import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print('работает')

@client.command()
async def load(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run('ODM0ODUyNTg5NjU2MzQyNTM4.YIG7EA.7C5dLOjMNLFJ9PXa-2S7kh2SE9A')