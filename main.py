import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    praise_john = '<:praisejohn:751866320315744330>'
    crying_ducc = '<:cryingducc:751955222401646694>'
    
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Teehee, hello!')

    if message.content.startswith('omegalul'):
        await message.channel.send('poggers')

    if message.content.startswith('DAILY'):
        await message.add_reaction('🇩')
        await message.add_reaction('🇦')
        await message.add_reaction('🇮')
        await message.add_reaction('🇱')
        await message.add_reaction('🇾')
        await message.add_reaction(praise_john)

    if message.content.startswith('PRAISE'):
        await message.add_reaction('🇵')
        await message.add_reaction('🇷')
        await message.add_reaction('🇦')
        await message.add_reaction('🇮')
        await message.add_reaction('🇸')
        await message.add_reaction('🇪')
        await message.add_reaction(praise_john)

    if message.content.startswith('JOHNO'):
        await message.add_reaction('🇯')
        await message.add_reaction('🇴')
        await message.add_reaction('🇭')
        await message.add_reaction('🇳')
        await message.add_reaction('🅾️')
        await message.add_reaction(praise_john)
    elif message.content.startswith('JOHN'):
        await message.add_reaction('🇯')
        await message.add_reaction('🇴')
        await message.add_reaction('🇭')
        await message.add_reaction('🇳')
        await message.add_reaction(praise_john)

    if message.content.startswith('sad'):
        await message.channel.send(crying_ducc)


client.run(os.getenv('TOKEN'))