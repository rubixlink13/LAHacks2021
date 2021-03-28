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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="My Love(내사랑)"))



@client.event
async def on_message(message):
    author = message.author.mention
    reaction_dict = {'praise_john': '<:praisejohn:751866320315744330>', 
	'bibble': '<:bibble:751866318705262593>', 'crying_ducc': 
	'<:cryingducc:751955222401646694>', 'eyes': '👀', 'bruh': 
	'<:bruh:751869125076189224>'}
    response_dict = {'hello': f'~Teehee, hello {author}~', 'omegalul' : 
	'poggers', 'wait': 'sus👖', 'smae': 'smae', 'sad': 
	reaction_dict['crying_ducc'], 'bruh': reaction_dict['bruh'],
    'smh': 'smh', '<:cutie:751869125130846288>': 'what a cutie', 'simp' : '<:simp:751866320726786138>'}
    ikr_arr = ['smh', 'imagine']
    
    
    split_msg = message.content.lower().split()
    
    if message.author == client.user:
        return
    elif message.content in reaction_dict.values():
        await message.channel.send(message.content)
    elif message.content.lower() in response_dict:
        await message.channel.send(response_dict[message.content.lower()])
    elif message.content in praise_dict.keys():
        await praise_dict[message.content](message)
        await message.add_reaction(reaction_dict['praise_john'])
    elif "i'm" in split_msg or "i’m" in split_msg:
        for index in range(len(split_msg)-1):
          if(split_msg[index] == "i'm" or split_msg[index] == "i’m"):
            name = ' '.join(split_msg[index+1:])
            await message.channel.send(f'hi {name}, nice to meet you hehe')
            return
    elif 'ty' in split_msg:
        await message.channel.send('tea why')
    elif 'nightmare' in split_msg:
        await message.channel.send('nightmare')
    elif split_msg[0] in ikr_arr:
        await message.channel.send(f'ikr {message.content.lower()}')
    elif 'better' in message.content.lower():
        for index in range(len(split_msg)-1):
            if(split_msg[index] == "better"):
                name = ' '.join(split_msg[index+1:])
                await message.channel.send(f'yeah feel better {name} :((')
                return

