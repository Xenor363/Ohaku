import nextcord, os
from nextcord.ext import commands

bot = commands.Bot(command_prefix="#", intents=nextcord.Intents.all())
#remove help command
bot.remove_command("help")

@bot.event
async def on_ready():
  print("Bot is ready!")

@bot.command()
async def load(ctx, extension):
  await ctx.message.delete()
  if ctx.author.id != 1138597370716766248:
    return
  bot.load_extension(f"cogs.{extension}")
  await ctx.send(f"Включена ветка : {extension}")
@bot.command(
  aliase=["cogs"]
)
async def reload(ctx, extension):
  await ctx.message.delete()
  if ctx.author.id != 1138597370716766248:
    return
  bot.reload_extension(f"cogs.{extension}")
  await ctx.send(f"Перезагружена ветка : {extension}")

@bot.command(
  aliase=["cogs"]
)
async def unload(ctx, extension):
  await ctx.message.delete()
  if ctx.author.id != 1138597370716766248:
    return
  bot.unload_extension(f"cogs.{extension}")
  await ctx.send(f"Отключена ветка : {extension}")
  
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
    print(f"Loaded {filename[:-3]}")

bot.run("MTIzMDQxNTIyMDk4ODQ0NDczMg.GLEROK.7giETQpfaLb1XtHiNenF0l71iizJdDlzLntHLw")