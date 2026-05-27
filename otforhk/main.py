import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import instaloader
import asyncio
import random
from io import BytesIO
import aiohttp
import datetime

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.all()
client = discord.Client(intents=discord.Intents.default())
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
intents.voice_states = True
bot = commands.Bot(command_prefix="/", intents=intents)
gif = "https://tenor.com/view/miyabi-hoshimi-miyabi-miyabi-happy-miyabi-laugh-laugh-gif-5523255195478659010"
gif2 = "https://tenor.com/view/miyabi-hoshimi-miyabi-zzz-disagreement-disagree-gif-2514870511680637718"
gif3 = "https://tenor.com/view/hoshimi-miyabi-miyabi-zenless-zone-zero-zzz-hoyoverse-gif-6374051001262459062"
painduxe = 678581104810131456
INSTAGRAM_USERNAME = "otforhk"
L = instaloader.Instaloader()
USERS_TO_DM = [
    783688506479607859,
    678581104810131456,  # User 1 ID
    628918103207837758,  # User 2 ID
]
text = [
    "People often ask what is Occupational Therapy? Simply due to lack of prior knowledge or awareness of a rather niche field of healthcare. So let me introduce you to Occupational Therapy: Occupational Therapy or OT is a field that improves quality of life through environmental modifications, education of everyday skills and promotion of healthy living. In other words, OT helps clients take part in daily activities and routines in rehabilitation. Now you know!",
    "Falls are the top cause of injury among elderly. Slippery floors at home make daily life risky. This Christmas, keep your grandparents warm and safe by gifting them a simple pair of grip socks. Like, Follow and Share to support my content on everyday occupation",
    "Swollen legs, or edema, is often linked with old age or a sedentary lifestyle. Skeletal muscles become weak & contract less --> blood flow decreases --> tissue fluid accumulates --> swelling occurs 🧦Compression socks offer a remedy by applying gentle pressure to the legs and feet, promoting venous return and improving blood circulation ✨ Look for breathable & stretchable compression socks when purchasing for family, ideally the ones that cover the calf muscles ⚠️ If they have medical conditions like diabetes, always consult an OT or PT professional first, since specific compression levels may be required",
    "In the forearm, the radial bone overlaps with the ulnar bone whenever we are using a regular mouse to browse the internet, compile powerpoint presentations, or to play online games. This places stress on the forearm muscles and nerves which may result in several injuries and health risks such as Carpal Tunnel. To prevent this, opt for ergonomic mouses that are designed for comfort when we use our computers. They are often cheap and you can find them in hardware stores on the street. It will definitely be a long term investment to stay injury-free in this age where computers are a commonplace in our daily lives.",
]
text2 = [
    (
        "0 cycle all knights stages",
        "Knight 1: Superbreak Knight 2: DoT Knight 3: Castorice",
    ),
    ("My first ever triple in a character banner", "2nd pic is my honest reaction"),
    ("Day 1 Trigger build", "my mediocre trigger build"),
    ("Day 1 Astra build", "#AstraYao"),
    ("Possibly the best disc 5 pull", "maybe my miyabi gacha luck went to this disc"),
    (
        "I DID IT MIYABROS",
        "After not pulling for anyone except for burnice, I got M6S1 after 700ish pulls. Could have saved some money if I waited for more free polychromes from upcoming events, but my impatient ahh spent around $200 to get her to m6 and it was so worth it. Hope all miyabros won their 50/50s and got her",
    ),
    (
        "I GOT HER",
        "I really like her design and character demo so I immediately went on zzz when the banner reset and I brought her home early within 70 pulls. Although i still have around 11000 polychromes, im probably gonna skip her w engine to save for queen miyabi",
    ),
]


@bot.event
async def on_ready():
    print(f"/networth")


def get_greeting():
    current_hour = (datetime.datetime.now().hour + 8) % 24

    if 5 <= current_hour < 12:
        return "Good Morning! ☀️"
    elif 12 <= current_hour < 17:
        return "Good Afternoon! 🌤️"
    elif 17 <= current_hour < 21:
        return "Good Evening! 🌙"
    else:
        return "Good Night! 🌚"


@bot.command()
async def yap(ctx):
    post = random.choice(text)
    await ctx.send(post)


@bot.command()
async def hoyo(ctx):
    post2 = random.choice(text2)
    with open("painduxe.png", "rb") as f:
        file = discord.File(f, filename="painduxe.png")

    embed = discord.Embed(
        title=post2[0],
        description=post2[1],
        color=discord.Color.green(),
        timestamp=discord.utils.utcnow(),
    )
    embed.set_thumbnail(url="attachment://painduxe.png")
    await ctx.send(file=file, embed=embed)


@bot.command()
async def mention(ctx):
    user = await bot.fetch_user(painduxe)
    for i in range(1, 4):
        await ctx.send(f"{user.mention}")


@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id == 710143953533403226:
        await message.channel.send(
            f"Hey {message.author.mention}! Stop it get some help!"
        )

    if "miyabi" in message.content.lower():
        await message.channel.send(f"did someone just send miyabi")
        await message.channel.send(gif)

    if "67" in message.content.lower():
        for i in range(1, 4):
            await message.channel.send(67)

    if "otforhk" in message.content.lower():
        greeting = get_greeting()
        await message.channel.send(f"{greeting} {message.author.mention}")
        await message.channel.send(f"How can I help you today?")

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
                    timestamp=discord.utils.utcnow(),
                )
                embed.add_field(
                    name="Channel", value=after.channel.mention, inline=True
                )
                embed.add_field(name="Server", value=member.guild.name, inline=True)
                embed.add_field(
                    name="Members in Call",
                    value=len(after.channel.members),
                    inline=True,
                )

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
async def fight(ctx):
    await ctx.send(gif3)


@bot.command()
async def networth(ctx):
    for i in range(1, 4):
        await ctx.send(67)


@bot.command()
async def pain(ctx):
    await ctx.send(
        "https://www.instagram.com/p/DYzsnyZGhUu/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="
    )


@bot.command()
async def cmd(ctx):
    word = """
    **Commands:**
    /no
    /fight
    /networth
    /fox
    /hello
    /hoyo
    /yap
    """
    await ctx.send(word)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
