import discord
from discord.ext import  commands
import logging
from dotenv import load_dotenv
import os 

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True 
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Bố {bot.user.name} tới rồi đây!!!")


@bot.event
async def on_member_join(member):
    await member.send(f'Hello {member.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.channel.send(f"Hey {message.author.mention} watch your fucking mouth")

    if 'kiem' in message.content.lower():
        await message.channel.send(f"Chính thái bò, hốc trưởng, ngủ trương dái đến 2h trưa")

    await bot.process_commands(message)


# !yo
@bot.command()
async def yo(ctx):
    await ctx.send(f'Hello thg l {ctx.author.mention}')

@bot.command()
async def reply(ctx):
    await ctx.reply(f'Kêu kêu cái cc!!!')

bot.run(token=token, log_handler=handler, log_level=logging.DEBUG)


print("Stop!!!")