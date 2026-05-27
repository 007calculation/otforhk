import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.default())
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix='/', intents=intents)
gif = "https://tenor.com/view/miyabi-hoshimi-miyabi-miyabi-happy-miyabi-laugh-laugh-gif-5523255195478659010"
gif2 = "https://tenor.com/view/miyabi-hoshimi-miyabi-zzz-disagreement-disagree-gif-2514870511680637718"
painduxe = 678581104810131456

USERS_TO_DM = [
    783688506479607859
    #678581104810131456,  # User 1 ID
    #628918103207837758   # User 2 ID
]
@bot.event
async def on_ready():
    print(f"/networth")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.author.id == 710143953533403226:
        await message.channel.send(f"Hey {message.author.mention}! Stop it get some help!")
    
    if "miyabi" in message.content.lower():
        await message.channel.send(f"did someone just send miyabi")
        await message.channel.send(gif)

    if "67" in message.content.lower():
        for i in range(1, 4):
            await message.channel.send(67)

    await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:

        for user_id in USERS_TO_DM:
            try:
                user = await bot.fetch_user(user_id)
                
                embed = discord.Embed(
                    title="🔊 Voice Call Started!",
                    description=f"join the call la bro",
                    color=discord.Color.green(),
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Channel", value=after.channel.mention, inline=True)
                embed.add_field(name="Server", value=member.guild.name, inline=True)
                embed.add_field(name="Members in Call", value=len(after.channel.members), inline=True)
                
                await user.send(embed=embed)
                print(f"✅ DM sent to {user.name}")
                
            except discord.Forbidden:
                print(f"❌ Cannot DM user {user_id} - DMs disabled")
            except Exception as e:
                print(f"❌ Error: {e}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")

@bot.command()
async def fox(ctx):
    await ctx.send(gif)

@bot.command()
async def no(ctx):
    await ctx.send(gif2)

@bot.command()
async def networth(ctx):
    for i in range(1, 4):
        await ctx.send(67)

@bot.command()
async def pain(ctx):
    await ctx.send("https://www.instagram.com/p/DYzsnyZGhUu/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
