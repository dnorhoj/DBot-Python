import discord, config
from discord.ext import commands

class Help():
	def __init__(self, bot):
		self.bot = bot

	def addfooter(self, embed):
		embed.set_footer(text="This bot was made by @dnorhoj#1337")
		return embed

	# Help command
	@commands.group(invoke_without_command=True)
	async def help(self, ctx):
		embed = discord.Embed(title="Command list", description="Command categories.", color=0xffd700)
		embed.add_field(name=":tada: Fun commands", value="`{0.prefix}{0.invoked_with} fun`".format(ctx), inline=True)
		embed.add_field(name=":hash: Hashing/encoding", value="`{0.prefix}{0.invoked_with} encoding`".format(ctx), inline=True)
		await ctx.send(embed=self.addfooter(embed))
	
	@help.group()
	async def fun(self, ctx):
		embed = discord.Embed(title=":tada: Fun commands", description="Games, and fun commands.", color=0xffd700)
		embed.add_field(name="Minesweeper", value="Made with discord spoilers\n`{}minesweeper`".format(ctx.prefix), inline=True)
		embed.set_footer(text="This bot was made by @dnorhoj#1337")
		await ctx.send(embed=self.addfooter(embed))
		
	@help.group(aliases=["hashing", "coding", "decoding"])
	async def encoding(self, ctx):
		embed = discord.Embed(title=":hash: Hashing/encoding", description="Get some encoding/decoding done fast.", color=0xffd700)
		embed.add_field(name="Base64", value="Encode/decode base64\n`{}base64`".format(ctx.prefix), inline=True)
		embed.add_field(name="Base32", value="Encode/decode base32\n`{}base32`".format(ctx.prefix), inline=True)
		embed.add_field(name="Coming soon", value="MD5, SHA512, etc.", inline=True)
		embed.set_footer(text="This bot was made by @dnorhoj#1337")
		await ctx.send(embed=self.addfooter(embed))

def setup(bot):
	bot.add_cog(Help(bot))
	return True