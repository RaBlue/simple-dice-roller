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
async def on_ready():
    channel = bot.get_channel(dontlook.get_test_channel_id())
    #initialize default dice
    global d0 
    d0 = dice.Dice()
    global d4 
    d4 = dice.Dice()
    d4.d4()
    global d6 
    d6 = dice.Dice()
    d6.d6()
    global d8 
    d8 = dice.Dice()
    d8.d8()
    global d10 
    d10 = dice.Dice()
    d10.d10()
    global d12 
    d12 = dice.Dice()
    d12.d12()
    global d20 
    d20 = dice.Dice()
    d20.d20()
    global d100 
    d100 = dice.Dice()
    d100.d100()
    #sends message to channel when bot is online
    await channel.send('Dice God watches you...') 

#Dice God's commands

@bot.command()
#returns which profile you are using
async def whoami(ctx):
    await ctx.send("You are you.")
#@bot.command()
#async def check(ctx):
    #d4.d4()
    #await ctx.send("Sides: {}, Modifier: {}, Damage Type: {}, Name: {}".format(d4.sides(), d4.mod(), d4.dmg(), d4.name()))

@bot.command()
#rolls a die of any size and modifier with advantage or disadvantage x number of times
#checks to see if die is default, if not creatres custom die
async def roll(ctx,die='d20', mod='0', weight='n', numRolls='1'):
    if die == 'd4':
        d4.setMod(mod)
        for i in range(int(numRolls)):
            #await ctx.send("You rolled a {} on a {} adding {} and rolling with {}".format(d4.rollDice(weight,numRolls),die,mod,weight))
            d4.rollDice(weight,d4.mod())
            await ctx.send(d4.resultText())
    elif die == 'd6':
        d6.setMod(mod)
        for i in range(int(numRolls)):
            d6.rollDice(weight,d6.mod())
            await ctx.send(d6.resultText())
    elif die == 'd8':
        d8.setMod(mod)
        for i in range(int(numRolls)):
            d8.rollDice(weight,d8.mod())
            await ctx.send(d8.resultText())
    elif die == 'd10':
        d10.setMod(mod)
        for i in range(int(numRolls)):
            d10.rollDice(weight,d10.mod())
            await ctx.send(d10.resultText())
    elif die == 'd12':
        d12.setMod(mod)
        for i in range(int(numRolls)):
            d12.rollDice(weight,d12.mod())
            await ctx.send(d12.resultText())
    elif die == 'd20':
        d20.setMod(mod)
        for i in range(int(numRolls)):
            d20.rollDice(weight,d20.mod())
            await ctx.send(d20.resultText())
    elif die == 'd100':
        d100.setMod(mod)
        for i in range(int(numRolls)):
            d100.rollDice(weight,d100.mod())
            await ctx.send(d100.resultText())
    #error handling to check if die can be created
    elif error_handling.numValidation(die) == True:
         d0.custom(die,mod,'0','custom')
         for i in range(int(numRolls)):
            d0.rollDice(weight,d0.mod())
            await ctx.send(d0.resultText())
    else:
        await ctx.send("Invalid input. When rolling a custom die, please use the format !roll <# of sides> <modifier> <a or d> <# of rolls>.")

   # rolls = abs(int(numRolls))
    #for i in range(rolls):
    #    await ctx.send(die, mod, weight)

@bot.command()
#adds multiple die rolls together   
async def multi(ctx, numDice):
    await ctx.send("You dealt " + (numDice) + " in damage!")

@bot.command()
#dont remember what this was for, probably for testing or a workaround
async def message(ctx,text):
    await ctx.send(text)  

    
    
    

#this makes the bot run
bot.run(dontlook.get_token())