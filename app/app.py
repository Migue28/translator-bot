import discord
import os
from dotenv import load_dotenv
import re
from services.translator import translate_text

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if re.findall("^!!", user_message):
        translated_text = translate_text(user_message, 'es')
        clean_text = translated_text[2:]
        await message.channel.send(clean_text)
        return


client.run(os.getenv("DISCORD_TOKEN"))