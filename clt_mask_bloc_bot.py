from discord.ext import tasks
import discord, os, logging, time

TOKEN = os.getenv("TOKEN")
REACTION_MESSAGE_ID = os.getenv("REACTION_MESSAGE_ID")
DRIVING_REACTION_ROLE_ID = os.getenv("DRIVING_REACTION_ROLE_ID")
SUPPORTER_ROLE_ID = os.getenv("SUPPORTER_ROLE_ID")
WELCOME_CHANNEL_ID = os.getenv("WELCOME_CHANNEL_ID")

WELCOME_MESSAGE = """

hello!"""

logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

role_id_dict = {
    ":articulated_lorry:": DRIVING_REACTION_ROLE_ID
}

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
async def on_raw_reaction_add(reaction: discord.RawReactionActionEvent):
    logger.info(reaction.emoji.name)
    if reaction.message_id == int(REACTION_MESSAGE_ID):
        role = client.get_guild(reaction.guild_id).get_role(role_id_dict[reaction.emoji.name])
        if not role in reaction.member.roles:
            await reaction.member.add_roles(role)
            logger.info(f"User Id {reaction.member.id}, Name {reaction.member.name} recieved {role.name} role")

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
