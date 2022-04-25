import discord
import random
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio
from asyncio import sleep
import http.client

#Steps if reinstall
# 1. Reinstall Python
# 2. Install FFMPeg
# 3. Install pynacl
# 4. Create Config.py

# importing sys
import sys

# adding Folder_2 to the system path
sys.path.insert(0, '\config\config.py')

# importing the add and odd_even 
# function
from config.config import BotToken

#cd C:\Users\johar\OneDrive\Desktop\Discord.py
#python3 bot.py


client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready():
	print('The machine has awaken.')

#Ping module
@client.command()
async def ping(ctx):
        await ctx.send(f'-+HAIL RECEIVED AT {round(client.latency *1000)}ms+-')

#8ball Module
@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
        responses = ['+The OMNISSIAH wills it to be so+',
                     '+THY WILL BE DONE+',
                     '+THE NUMBERS SAY SO+',
                     '+LOGIC COGITATORS : Yes+',
                     '+LOGIC COGITATORS : Certain+',
                     '+LOGIC COGITATORS : 99.999999%+',
                     '+YES+',
                     '+SUCCESS CHANCE : 85.33%+',
                     '+SUCCESS CHANCE : 90.00%+',
                     '+OUTCOME : GOOD+',
                     '+SUCCESS CHANCE : HIGH+',
                     '+WHY WOULD YOU EVEN ASK THAT+',
                     '+INDICATIONS CONFUSED : Try Again+',
                     '+THE SPIRITS ARE UNCERTAIN+',
                     '+LOGIC COGITATORS : 50%+',
                     '+Machine does not compute : Try Again+',
                     '+ACCESS DENIED : USER LEVEL DOES NOT ALLOW INQUIRY+',
                     '+LOGIC COGITATORS : [++REDACTED++] -USER LEVEL INSUFFICIENT FOR ANSWER-+',
                     '+UNEXPECTED_STORE_EXCEPTION  -INQUIRY INCALCULABLE-+',
                     '+INSUFFICIENT PRAYER FOR ANSWER',
                     '+LOGIC COGITATORS : 0.01%.+',
                     '+SUCCESS CHANCE : 3.142%.+',
                     '+[++REDACTED++]+',
                     '+NO+',
                     '+OUTCOME : Not Likely+',
                     '+PRAY HARDER+',
                     '+OMNISSIAH PRESERVE US FROM THIS OUTCOME+',
                     '+CATASTROPHIC FAILURE+',
                     '+CONTACT LORD-CREATOR JO FOR MORE INFO+',
                     '+THE SPIRITS ARE CERTAIN IT WILL NOT BE SO+',
                     '+HIGH-GOTHIC : NEIN   LOW-GOTHIC : NO+',
                     '+THE NUMBERS ARE AGAINST IT+',
                     '+PROCEED WITH CAUTION+'
                     ]

        #await ctx.send(f'+INQUIRY : "{question}"+\n\n{random.choice(responses)}')
        #await ctx.send(f'{random.choice(responses)}')
        answer = f'{random.choice(responses)}'
        myEmbed = discord.Embed(title ="LOGIC COGITATORS" ,color=0xD72C2C)
        myEmbed.add_field(name = f'INQUIRY : "{question}"',value = "." ,inline=False)
        myEmbed.add_field(name = answer, value=".", inline=False)
        await ctx.send(embed=myEmbed)


#Join Voice chat Module
@client.command(pass_context = True)
async def join(ctx):
        if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('join.mp3')
                player = voice.play(source)
                #await ctx.send("-+ORDERS RECEIVED : JOINING VOX CHANNEL+-")
        else:
                await ctx.send("-+ERROR : USER NOT IN VOX CHANNEL+-")

        while voice.is_playing(): #Checks if voice is playing
                await asyncio.sleep(1) #While it's playing it sleeps for 1 second
        else:
                await asyncio.sleep(5) #If it's not playing it waits 5 seconds
                while voice.is_playing(): #and checks once again if the bot is not playing
                        break #if it's playing it breaks
                else:
                        await voice.disconnect() #if not it disconnects

#Play songs module
@client.command(pass_context = True, aliases=['p'])
async def play(ctx,*,song):
        if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()

                 #---------------Memes----------------------------------#

                if (song == 'tikus'):
                        source = FFmpegPCMAudio('tikus.mp3')
                        player = voice.play(source)

                if (song == 'sting'):
                        source = FFmpegPCMAudio('sting.mp3')
                        player = voice.play(source)

                if (song == '17pdr' or song == 'firefly'):
                        source = FFmpegPCMAudio('17pdr.mp3')
                        player = voice.play(source)

                if (song == 'Drinking Song' or song == 'drinking song'):
                        source = FFmpegPCMAudio('Drinking Song.mp3')
                        player = voice.play(source)

                if (song == 'Chemistry' or song == 'chemistry'):
                        source = FFmpegPCMAudio('chemistry.mp3')
                        player = voice.play(source)
                
                if (song == 'Cicada' or song == 'cicada'):
                        source = FFmpegPCMAudio('cicada.mp3')
                        player = voice.play(source)

                if (song == 'angry'):
                        source = FFmpegPCMAudio('angry.mp3')
                        player = voice.play(source)

                if (song == 'study' or song == 'terlambat'):
                        source = FFmpegPCMAudio('study.mp3')
                        player = voice.play(source)

                if (song == 'diam' ):
                        source = FFmpegPCMAudio('diam.mp3')
                        player = voice.play(source)

                if (song == 'semangat'):
                        source = FFmpegPCMAudio('semangat.mp3')
                        player = voice.play(source)

                if (song == 'nipah'):
                        source = FFmpegPCMAudio('nipah.mp3')
                        player = voice.play(source)



                #---------------VI----------------------------------#

                if (song == '125'):
                        source = FFmpegPCMAudio('125.mp3')
                        player = voice.play(source)

                if (song == 'school song' or song == 'School Song'):
                        source = FFmpegPCMAudio('school song.mp3')
                        player = voice.play(source)


                 #---------------Songs----------------------------------#

                if (song == 'hail'):
                        source = FFmpegPCMAudio('hail.mp3')
                        player = voice.play(source)

                if (song == 'Fateful Night' or song == 'fateful night'):
                        source = FFmpegPCMAudio('Fateful Night.mp3')
                        player = voice.play(source)

                if (song == 'Another Voice' or song == 'another voice'):
                        source = FFmpegPCMAudio('Another Voice.mp3')
                        player = voice.play(source)

                if (song == 'Tragedy' or song == 'tragedy'):
                        source = FFmpegPCMAudio('Tragedy.mp3')
                        player = voice.play(source)

                if (song == 'Hope' or song == 'hope'):
                        source = FFmpegPCMAudio('hope.mp3')
                        player = voice.play(source)

                if (song == 'Legacy' or song == 'legacy'):
                        source = FFmpegPCMAudio('legacy.mp3')
                        player = voice.play(source)
                
                if (song == 'oorai' or song == 'Oorai'):
                        source = FFmpegPCMAudio('oorai.mp3')
                        player = voice.play(source)

                if (song == 'golden hour' or song == 'golden'):
                        source = FFmpegPCMAudio('goldenHour.mp3')
                        player = voice.play(source)
                
                if (song == 'Hikatanoi' or song == 'hikatanoi'):
                        source = FFmpegPCMAudio('Hikatanoi.mp3')
                        player = voice.play(source)


                while voice.is_playing(): #Checks if voice is playing
                        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
                else:
                        await asyncio.sleep(5) #If it's not playing it waits 5 seconds
                        while voice.is_playing(): #and checks once again if the bot is not playing
                                break #if it's playing it breaks
                        else:
                                await voice.disconnect() #if not it disconnects



#Leave Module
@client.command(pass_context = True)
async def leave(ctx):
        if (ctx.voice_client):
                await ctx.guild.voice_client.disconnect()
                #await ctx.send("-+ORDERS RECEIVED : LEAVING VOX CHANNEL+- \n \n -+THE OMNISSIAH PROTECTS+-")
        else:
                await ctx.send("-+ERROR : THE SPIRIT IS NOT IN A VOX CHANNEL+-")

@client.command()
async def helps(ctx):
        myEmbed = discord.Embed(title ="TECHNICAL MANUAL" ,color=0xD72C2C)
        myEmbed.add_field(name = f'+ping',value = "Enquire Machine Response time" ,inline=False)
        myEmbed.add_field(name = f'+8ball [QUESTION]', value="Invoke the Logic Cogitators for decision making", inline=False)
        myEmbed.add_field(name = f'+join', value="Invoke the Symphonium Cogitators to join the Vox channel", inline=False)
        myEmbed.add_field(name = f'+join', value="Command the Symphonium Cogitators to leave the Vox channel", inline=False)
        myEmbed.add_field(name = f'+play [SONG]', value="Invoke the Tune developed from the Adeptus Symphonicus \n", inline=False)
        await ctx.send(embed=myEmbed)

@client.command()
async def song(ctx):
        myEmbed = discord.Embed(title ="SYMPHONIUM COGITATORS" ,color=0xD72C2C)
        myEmbed.add_field(name = f'+MEMES+', value="---------------------------", inline=False)
        myEmbed.add_field(name = f'+17pdr',value = "17 Pounder Firefly meme" ,inline=False)
        myEmbed.add_field(name = f'+sting', value="Sting Aku Yahoo", inline=False)
        myEmbed.add_field(name = f'+tikus', value="GUYS TIKUS GUYS", inline=False)
        myEmbed.add_field(name = f'+angry', value="Angry Chinese man meme aka CAO NI MA \n", inline=False)
        myEmbed.add_field(name = f'+chemistry', value="Paan reciting Chemistry textbook", inline=False)
        myEmbed.add_field(name = f'+diam', value="DIAM LA B!@#H", inline=False)
        myEmbed.add_field(name = f'+study', value="Awal sem dulu taknak study", inline=False)
        myEmbed.add_field(name = f'+semangat', value="Jangan patah semangat", inline=False)
        myEmbed.add_field(name = f'+nipah', value="Rika Nipah", inline=False)

        myEmbed.add_field(name = f'+VI+', value="---------------------------", inline=False)
        myEmbed.add_field(name = f'+125', value="VI Centenary song", inline=False)
        myEmbed.add_field(name = f'+school song', value="VI School song \n", inline=False)

        myEmbed.add_field(name = f'+ECHO THROUGH ETERNITY+', value="---------------------------", inline=False)
        myEmbed.add_field(name = f'+another voice', value="Another Voice Calls out from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+drinking song', value="For the Land That I Come From (Ctrigall Drinking Song) from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+fateful night', value="On That Fateful Night from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+tragedy', value="Bonded by Tragedy from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+hail', value="Hail Leidenschaftlich! from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+hope', value="A Young Boy's Hope from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+legacy', value="Violet Evergarden's Legacy from Violet Evergarden Movie OST", inline=False)
        myEmbed.add_field(name = f'+oorai', value="Girls und Panzer Daikon War OVA song", inline=False)
        myEmbed.add_field(name = f'+golden hour', value="Golden Hour – Vlad Gluschenko (No Copyright Music)", inline=False)


        await ctx.send(embed=myEmbed)
  


import os

path = "C:\Songs"
all_mp3 = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
randomfile = random.choice(all_mp3)

@client.command(pass_context = True)
async def stuff(ctx):
        
        async def randomSong():
                randomfile = random.choice(all_mp3)

                source = FFmpegPCMAudio(randomfile)
                player = voice.play(source)
                myEmbed = discord.Embed(title ="NOW PLAYING :" ,color=0xD72C2C)
                myEmbed.add_field(name = f'{randomfile[9:-4]}',value = "." ,inline=False)
                print(randomfile)
                await ctx.send(embed=myEmbed)

        # async def embed():
        #         myEmbed = discord.Embed(title ="NOW PLAYING :" ,color=0xD72C2C)
        #         myEmbed.add_field(name = f'{randomfile[9:-4]}',value = "." ,inline=False)
        #         await ctx.send(embed=myEmbed)
                
        
        if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                voice = await channel.connect()


                await randomSong()
                # await embed()

        async def checkSong():

                while voice.is_playing(): #Checks if voice is playing
                        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
                else:
                                await randomSong()
                                print("End song")
                                await checkSong()
                                # await voice.disconnect() #if not it disconnects

        await checkSong()


client.run(BotToken)