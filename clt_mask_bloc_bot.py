from discord.ext import tasks
import discord, os, logging, time

TOKEN = os.getenv("TOKEN")
SUPPORTER_ROLE_ID = os.getenv("SUPPORTER_ROLE_ID")
WELCOME_CHANNEL_ID = os.getenv("WELCOME_CHANNEL_ID")

WELCOME_MESSAGE = """

hello!"""

logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# EVENTS

@client.event
async def on_ready():
    logger.info(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member: discord.Member):
    supporter_role = member.guild.get_role(int(SUPPORTER_ROLE_ID))
    await reaction.member.add_roles(supporter_role)
    await client.get_channel(int(WELCOME_CHANNEL_ID)).send(f"Welcome to Charlotte Mask Bloc, <@{member.id}> 🥳 !" + WELCOME_MESSAGE)
    logger.info(f"User Id {member.id}, Name {member.name} joined, recieved supporter role, and welcome message sent")

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
