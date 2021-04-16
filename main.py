import discord
import os
from datetime import datetime
import asyncio
import threading
import random

last_msg = dict()
last_time = '0:00'
morning_dict = dict()

three_am = '03:00'
seven_am = '07:00'

client = discord.Client()
friends_list = [
'<@!635960985416368149>', ' <@!354126467837329408>', 
'<@!290342028804620288>', '<@!497230240691519489>', 
'<@!589187026642010143>', '<@702286051326165083>',
'<@!627316223108972548>', '<@!345809706700374019>',
'<@!309555091608961024>', '<@!547982876877258792>', 
'<@!299243272176664577>', '<@!229087820273287171>',
'<@694030350350942247>'
]

quackheads = [
'<@!635960985416368149>', '<@!354126467837329408>', 
'<@!290342028804620288>', '<@!547982876877258792>',
'<@!229087820273287171>', '<@!345809706700374019>',
'<@!589187026642010143>', '<@!309555091608961024>'
]

qk_messages = [
f"Have a great day {random.choice(quackheads)}!", "Hope you're getting enough rest tonight {random.choice(quackheads)}!",
f"Please stay hydrated {random.choice(quackheads)}!", f"Hope you're having a great night {random.choice(quackheads)}!",
f"Please don't stay up all night long unless you have to, because I care about your health {random.choice(quackheads)}!",
f"Are you okay {random.choice(quackheads)}?", f"Good luck with whatever you're up to {random.choice(quackheads)}!"
]

bihour = ["00:00", "02:00", "04:00", "06:00", "08:00",
"10:00", "12:00", "14:00", "16:00", "18:00", "20:00",
"22:00"]

greeting = ["HELLO", "GREETINGS", "HENLO", "HOLA", "HI", "HEY",
"PRAISE", "HOPE YOUR YAMS ARE PROSPERING"]

pronoun = ["BROTHER", "DUDE", "GUY", "ASSOCIATE", "GOOD SIR",
"PEEP", "TIGER BUDDY"]

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

async def checkWishTime():
	# runs every minute
    global last_time
    global morning_dict
    channel = client.get_channel(751928157489201252)
    dootly = client.get_channel(752017650636292257)
    simp = client.get_channel(751856605087268897)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if(current_time != last_time):
        print(channel)
        print("Current Time =", current_time)
    
    if(current_time == last_time):
        pass
    elif(current_time == "00:00"):
        f = open("morning.txt", "w")
        f.close()
        morning_dict.clear()
    elif(current_time == "11:11" or current_time == "23:11"):
        await channel.send("OMG JOHN I FREAKING LOVE YOU YOU'RE THE BESTEST BFF4L EVER")
    elif(current_time == "22:00"):
        await dootly.send("Goodnight Sushi!")
    elif(current_time == "01:00"):
        await dootly.send("Goodnight Kenny!")
    elif(current_time == "02:00"):
        await dootly.send(random.choice(qk_messages))
    elif(current_time == "03:00"):
        await dootly.send("Goodnight Liz!")
        await dootly.send("Goodnight Brain!")
    
    if(current_time == last_time):
        pass
    elif(current_time in bihour):
        await simp.send(f"{random.choice(greeting)} {random.choice(friends_list)}, MY {random.choice(pronoun)}, THIS IS A RANDOM BI-HOURLY REMINDER THAT YOU ARE JOHN'S BEST FRIEND 4 LYFE AND HE LOVES YOU VERY VERY MUCH, HEHE OKIE BYE NOW")
    
    last_time = current_time
    await asyncio.sleep(59)
    await checkWishTime()

@client.event
async def on_ready():
    fetch_morning()
    announce = client.get_channel(763674650311131166)
    print('We have logged in as {0.user}'.format(client))
    #await announce.send("Kenelijaijoh has been updated! Probably due to one of your requests so try it out hehe! <:praisejohn:751866320315744330>")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="My Love(내사랑)"))
    await checkWishTime() 

def fetch_morning():
    global morning_dict
    if(os.path.exists("morning.txt")):
        f = open("morning.txt", "r")
        names = f.readline().split()
        for name in names:
            morning_dict[name] = True
    else:
        f = open("morning.txt", "w")
    f.close()

@client.event
async def on_message(message):
    author = message.author.mention
    reaction_dict = {'praise_john': '<:praisejohn:751866320315744330>', 
	'bibble': '<:bibble:751866318705262593>', 'crying_ducc': 
	'<:cryingducc:751955222401646694>', 'eyes': '👀', 'bruh': 
	'<:bruh:751869125076189224>', 'pain': '<:pain:751866319938257057>'}
    response_dict = {'hello': f'~Teehee, hello {author}~', 'omegalul' : 
	'poggers', 'wait': 'sus👖', 'smae': 'smae', 'hehe': 'teehee', 'teehee': 'hehe', 'sad': 
	reaction_dict['crying_ducc'], 'bruh': reaction_dict['bruh'],
	'interesting': "ain't that wacky", 'no': 'no ❤️', 'yes':
	'yes ❤️', 'nice': 'nice', "11:11": "MAKE A WISH!", 'sunday': 
	'DID SOMEONE SAY ATTACK ON TITAN SUNDAYS?!',
    'smh': 'smh','<:cutie:751869125130846288>': 'what a cutie', 
	'simp' : '<:simp:751866320726786138>', 'pain' :
	'<:pain:751866319938257057>'}

    ikr_arr = ['smh', 'imagine']
    
    tiger_fact = ['Tigers are the largest cat species in the world reaching up to 3.3 meters in length and weighing up to 670 pounds!',
    'Tigers are easily recognizable with their dark vertical stripes and reddish/orange fur.',
    'The Bengal tiger is the most common tiger.',
    'Tigers live between 20-26 years in the wild.',
    'Adult tigers generally live alone.',
    'Unlike most other cats, tigers are great swimmers and actually like the water.',
    'Cubs are born blind and only open their eyes 1-2 weeks after birth.',
    'Cubs start learning to hunt at six months of age but stay with their moms until they are about 18 months old.',
    'Tigers are stalk and ambush hunters; they lie in wait slowly creeping towards their prey until they are close enough to pounce.',
    'Tigers communicate using scent markings, visual signals and lots of sounds like roars, growls, snarls, grunts, moans, mews and hisses.',
    'Tigers are the largest amongst other wild cats',
    'A punch from a Tiger may kill you',
    'Tigers are nocturnal animals',
    'A group of Tigers are called an ambush or streak',
    'Tigers have antiseptic saliva',
    'Tigers can sprint at over 60 kilometre/hour',
    'Tiger stripes are also found on their skin',
    'Tigers rarely roar and are humble towards their group',
    'Tigers urine smells like buttered popcorn',
    'Tigers prefer to hunt by ambush',
    'Tigers do not normally view humans as a prey',
    'Tigers cannot purr',
    'John loves tigers']


    split_msg = message.content.lower().split()
    
    global last_msg    
    global morning_dict

    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if(message.channel not in last_msg):
        last_msg[message.channel] = message

    if message.author == client.user:
        return
    elif 'tiger fact' in message.content.lower():
        await message.channel.send(random.choice(tiger_fact))
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
    elif 'turtle' in split_msg:
        await last_msg[message.channel].add_reaction('🐢')
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
    elif 'perfect' in message.content.lower():
        await message.channel.send(f"No, YOU'RE perfect {author}")
    elif 'beautiful' in message.content.lower():
        await message.channel.send(f"No, YOU'RE beautiful {author}")
    elif "you're" in message.content.lower() or "you’re" in message.content.lower():
        await message.channel.send("no u")
    elif contains(split_msg, response_dict.keys()):
        await message.channel.send(response_dict[contains(split_msg, response_dict.keys())])
    elif str(message.author) not in morning_dict:
        morning_dict[str(message.author)] = True
        f = open("morning.txt", "a")
        f.write(str(message.author) + " ")
        await message.channel.send(f"GOOD MORNING {author}")
        f.close()
    elif (three_am <= now <= seven_am) and (message.author.id == 635960985416368149):
        await message.channel.send("go sleep liz !!")
    elif "shut up liz" in message.content.loser():
        await message.channel.send("yea shut up liz !!")
    

    last_msg[message.channel] = message

