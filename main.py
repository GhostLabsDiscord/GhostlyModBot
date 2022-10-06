import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix="g.", intents=intents)

@bot.event
async def on_ready():
  print(f"(bot.user.name) is ready!")

logging = True
logschannel = #copy your logs channel id

@bot.slash_command()
async def kick(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
  if not interaction.user.guild.permissions.administrator:
    await interaction.response.send_message("You are not authorized to run this command", epheneral=True)
  else:
      await interaction.response.send_message((f"Kicked by (user.mention"), epheneral=True)
      if logging is True:
        log_channel = bot.get.channel(logschannel)
        await log_channel.sent((f"(user.mention) was kicked by (interaction.user.mention"), epheneral=True)



@bot.slash_command()
async def ban(interaction: nextcord.Interaction, user: nextcord.Member, reason: str):
    if not interaction.user.guild.permissions.administrator:
       await interaction.response.send_message("You are not authorized to run this command", epheneral=True)
    else:
      await interaction.response.send_message(f"Banned by (user.mention)", epheneral=True)
      if logging is True:
        log_channel = bot.get.channel(logschannel)
        await log_channel.send(f"(user.mention) was banned by (interaction.user.mention) for (reason)")


bot.run("TOKEN")
