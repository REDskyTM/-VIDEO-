import discord
from discord.ext import commands
import os
import keep_alive

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
	print('работает')

@client.command()
async def load(ctx, extension):
	if ctx.author.id == ВАШ АЙДИ:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == ВАШ АЙДИ:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == ВАШ АЙДИ:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Ког загружен")
	else:
		await ctx.send("Вы не создатель бота")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

keep_alive.keep_alive()

my_secret = os.environ['TOKEN']

# Подключение бота
client.run(os.environ.get('TOKEN'), bot=True, reconnect =True)
