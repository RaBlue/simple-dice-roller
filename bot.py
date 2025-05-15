#bot commands, discord api and libraries
from discord.ext import commands
import discord
import random
import dice 
import error_handling
import dontlook


#command prefix to trigger bot ex: !help
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 

#Dice God's bot events
@bot.event
#What Dice God says when it boots up
async def on_ready():
    channel = bot.get_channel(dontlook.TEST_CHANNEL_ID)
    #sends message to channel when bot is online
    await channel.send('Dice God watches you...') 

#Dice God's commands
@bot.command()
#returns which profile you are using
async def whoami(ctx):
    await ctx.send("You are you.")
@bot.command()
#rolls a die of any size and modifier with advantage or disadvantage x number of times
async def roll(ctx,die, mod='0', weight='none', numRolls='1'):
    if error_handling.numValidation(numRolls) == False:
        await ctx.send("Invalid input. Please use the format !roll <die> <modifier> <a or d> <# of rolls>.")
        return
    rolls = abs(int(numRolls))
    for i in range(rolls):
        await ctx.send(die, mod, weight)
@bot.command()
#adds multiple die rolls together   
async def multi(ctx, numDice):
    await ctx.send("You dealt " + (numDice) + " in damage!")
@bot.command()
async def message(ctx,text):
    await ctx.send(text)  

    
    
    

#this makes the bot run
bot.run(dontlook.BOT_TOKEN)