import discord, base64, config
from discord.ext import commands

# pylint: disable=no-member

class Hashing():
	def __init__(self, bot):
		self.bot = bot
	
	# Base64 Commands
	@commands.group(invoke_without_command=True, aliases=["b64"]) # Create Fallback base64 command
	async def base64(self, ctx):
		await ctx.send("Usage: `{}base64 [encode/decode] [text]`".format(config.getPrefix(ctx.message.guild.id)))

	@base64.group(name="encode", aliases=["e"]) # Base64 encoding command
	async def b64encode(self, ctx, *, text:str):
		encoded = base64.b64encode(text.encode()).decode() # Encode text

		# Generate embed to send
		embed = discord.Embed(title=":white_check_mark: Encoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=encoded, inline=False)

		await ctx.send(embed=embed)

	@base64.group(name="decode", aliases=["d"]) # Base64 decoding command
	async def b64decode(self, ctx, *, text:str):
		decoded = base64.b64decode(text.encode()).decode() # Decode text
		
		# Generate embed to send
		embed = discord.Embed(title=":white_check_mark: Decoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=decoded, inline=False)

		await ctx.send(embed=embed)
	
	# Base32 Commands
	@commands.group(invoke_without_command=True, aliases=["b32"]) # Create Fallback base32 command
	async def base32(self, ctx):
		await ctx.send("Usage: `{}base32 [encode/decode] [text]`".format(config.getPrefix(ctx.message.guild.id)))

	@base32.group(name="encode", aliases=["e"]) # Base64 encoding command
	async def b32encode(self, ctx, *, text:str):
		encoded = base64.b64encode(text.encode()).decode() # Encode text

		# Generate embed to send
		embed = discord.Embed(title=":white_check_mark: Encoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=encoded, inline=False)

		await ctx.send(embed=embed)

	@base32.group(aliases=["d"]) # Base64 decoding command
	async def decode(self, ctx, *, text:str):
		decoded = base64.b64decode(text.encode()).decode() # Decode text
		
		# Generate embed to send
		embed = discord.Embed(title=":white_check_mark: Decoded Base64.", colour=0x00ff00)
		embed.add_field(name="Result", value=decoded, inline=False)

		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Hashing(bot))
	return True
