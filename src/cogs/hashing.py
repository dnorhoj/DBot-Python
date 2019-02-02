import discord, base64, config
from discord.ext import commands

# pylint: disable=no-member

class Hashing():
	def __init__(self, bot):
		self.bot = bot

	@commands.group(invoke_without_command=True, aliases=["b64"])
	async def base64(self, ctx):
		await ctx.send("Usage: `{}base64 [encode/decode] [text]`".format(config.getPrefix(ctx.message.guild.id)))

	@base64.group(aliases=["e"])
	async def encode(self, ctx, *, text:str):
		encoded = base64.b64encode(text.encode()).decode()

		embed = discord.Embed(title=":white_check_mark: Encoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=encoded, inline=False)

		await ctx.send(embed=embed)

	@base64.group(aliases=["d"])
	async def decode(self, ctx, *, text:str):
		decoded = base64.b64decode(text.encode()).decode()
		
		embed = discord.Embed(title=":white_check_mark: Decoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=decoded, inline=False)

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Hashing(bot))
	return True
