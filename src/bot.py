import discord, config
from discord.ext import commands

async def get_prefix(bot:commands.Bot, message):
	mention = "<@{}> ".format(bot.user.id)
	return [mention, "+"]

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
	print("""---Info---
	Successfully started.
	Running on user: {}
	---Info---""".replace("\t", "").format(bot.user))
	await bot.change_presence(activity=discord.Game("idk | +help"))

@bot.command()
async def oof(ctx):
	print(ctx.prefix)

# Define cogs to load
startup_extensions = [
	"cogs.help",
	"cogs.fun",
	"cogs.hashing"
]

# Load cogs
if __name__ == "__main__":
	lst = []
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
			lst.append(extension)
		except Exception as e:
			exc = "{}: {}".format(type(e).__name__, str(e))
			print("Failed to load {}\n{}".format(extension, exc))
	
	out = ", ".join(lst).replace("cogs.","")[::-1].replace(",", " and"[::-1], 1)[::-1]
	print("Loaded: {}".format(out))

# Start bot
bot.run(config.getSecret("TOKEN"))