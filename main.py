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

def contains(list1, list2):
    for obj1 in list1:
        if obj1 in list2:
            return obj1
    return False

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
	'<:bruh:751869125076189224>', 'pain': '<:pain:751866319938257057>'}
    response_dict = {'hello': f'~Teehee, hello {author}~', 'omegalul' : 
	'poggers', 'wait': 'sus👖', 'smae': 'smae', 'sad': 
	reaction_dict['crying_ducc'], 'bruh': reaction_dict['bruh'],
	'interesting': "ain't that wacky", 'no': 'no ❤️', 'yes':
	'yes ❤️', 'nice': 'nice', "11:11": "MAKE A WISH!", 'sunday': 
	'DID SOMEONE SAY ATTACK ON TITAN SUNDAYS?!',
    'smh': 'smh','<:cutie:751869125130846288>': 'what a cutie', 
	'simp' : '<:simp:751866320726786138>', 'pain' :
	'<:pain:751866319938257057>'}

    ikr_arr = ['smh', 'imagine']
    
    
    split_msg = message.content.lower().split()
    
    if message.author == client.user:
        return
    elif 'echo' == split_msg[0]:
        await message.channel.send(' '.join(split_msg[1:]))
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
    elif 'np' in split_msg:
        await message.channel.send('enn pee')
    elif 'nightmare' in split_msg:
        await message.channel.send('nightmare')
    elif split_msg[0] in ikr_arr and len(split_msg) > 1:
        await message.channel.send(f'ikr {message.content.lower()}')
    elif message.content in reaction_dict.values():
        await message.channel.send(message.content)
    elif 'better' in message.content.lower():
        for index in range(len(split_msg)-1):
            if(split_msg[index] == "better"):
                name = ' '.join(split_msg[index+1:])
                await message.channel.send(f'yeah feel better {name} :((')
                return
    elif 'hehe' in message.content.lower():
        await message.channel.send('teehee')
    elif 'teehee' in message.content.lower():
        await message.channel.send('hehe')
    elif 'perfect' in message.content.lower():
        await message.channel.send(f"No, YOU'RE perfect {author}")
    elif 'beautiful' in message.content.lower():
        await message.channel.send(f"No, YOU'RE beautiful {author}")
    elif "you're" in message.content.lower() or "you’re" in message.content.lower():
        await message.channel.send("no u")
    elif contains(split_msg, response_dict.keys()):
        await message.channel.send(response_dict[contains(split_msg, response_dict.keys())])

