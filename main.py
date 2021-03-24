import discord
import os

client = discord.Client()


async def react_daily(message):
    await message.add_reaction('🇩')
    await message.add_reaction('🇦')
    await message.add_reaction('🇮')
    await message.add_reaction('🇱')
    await message.add_reaction('🇾')

async def react_praise(message):
    await message.add_reaction('🇵')
    await message.add_reaction('🇷')
    await message.add_reaction('🇦')
    await message.add_reaction('🇮')
    await message.add_reaction('🇸')
    await message.add_reaction('🇪')

async def react_john(message):
    await message.add_reaction('🇯')
    await message.add_reaction('🇴')
    await message.add_reaction('🇭')
    await message.add_reaction('🇳')

async def react_johno(message):
    await message.add_reaction('🇯')
    await message.add_reaction('🇴')
    await message.add_reaction('🇭')
    await message.add_reaction('🇳')
    await message.add_reaction('🅾️')

praise_dict = {'DAILY': react_daily, 'PRAISE': react_praise, 'JOHN': react_john, 'JOHNO': react_johno}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    praise_john = '<:praisejohn:751866320315744330>'
    crying_ducc = '<:cryingducc:751955222401646694>'
    bibble = '<:bibble:751866318705262593>'
    author = message.author.mention
    response_dict = {'hello': f'~Teehee, hello {author}~', 'omegalul' : 'poggers', 'wait': 'sus👖', 'smae': 'smae', 'sad': crying_ducc}

    reaction_arr = [praise_john, bibble, crying_ducc]
    
    if message.author == client.user:
        return
    elif message.content in reaction_arr:
        await message.channel.send(message.content)
    elif message.content.lower() in response_dict:
        await message.channel.send(response_dict[message.content.lower()])
    elif message.content in praise_dict.keys():
        await praise_dict[message.content](message)
        await message.add_reaction(praise_john)
    elif message.content.startswith('smh'):
      split_msg = message.content.split()
      if(len(split_msg) > 1):
        await message.channel.send(f'ikr smh {split_msg[1]}')
      else:
        await message.channel.send('smh')


client.run(os.getenv('TOKEN'))