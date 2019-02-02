import discord
from discord.ext import commands

class Help():
	def __init__(self, bot):
		self.bot = bot

	# Help command
	@commands.group(invoke_without_command=True)
	async def help(self, ctx):
		await ctx.send("HELP")

	# Help command for fun commands.
	@help.group()
	async def fun(self, ctx):
		await ctx.send("example2")
	
	# Help command for moderation commands.
	@help.group()
	async def moderation(self, ctx):
		await ctx.send("Moderation")

	# Help command for owners
	@help.group()
	async def owner(self, ctx):
		await ctx.send("Owner")

def setup(bot):
	bot.add_cog(Help(bot))
	return True