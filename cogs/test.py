import discord
from discord.ext import commands

class test(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ['аватар'])
	async def avatar(self, ctx):
		await ctx.send(ctx.author.avatar_url)

def setup(client):
	client.add_cog(test(client))
	print("Ког тест работает")