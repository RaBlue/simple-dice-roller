#bot commands, discord api and libraries
from discord.ext import commands
import discord
import random
import error_handling


#Dice class
class Dice:
    def __init__(self, name='new dice', die=0, modifier=0):
        if error_handling.numValidation(die) == False or error_handling.numValidation(modifier) == False:
            return "Invalid input. Please enter a number."
        self.dName = name
        self.side = abs(int(die))
        self.modifier = modifier
        self.dmgType = ['none', 'bludgeoning', 'piercing', 'slashing', 'fire', 'cold', 'lightning', 'thunder', 'acid', 'poison']
        self.element = self.dmgType[0]
        self.lRoll = 0
        self.lMod = 0
        self.sRolls = []
        self.result = "You haven't rolled yet!"

    # DICE ATTRIBUTES
    def setName(self, name):
        self.dName = name

    def name(self):
        return self.dName

    def setSide(self, sides):
        if error_handling.numValidation(sides) == False:
            return "Invalid input. Please enter a number."
        self.side = abs(int(sides))

    def sides(self):        
        return self.side

    def setMod(self, modifier):
        if error_handling.numValidation(modifier) == False:
            return "Invalid input. Please use the format !roll <die> <modifier>."
        self.modifier = int(modifier)
    
    def mod(self):
        return self.modifier    

    #sets dice dmg type
    def setDmg(self, type):
        if error_handling.numValidation(type) == False:
            return "Invalid input. Please enter a number."
        else:
            self.element = self.dmgType[abs(int(type))]

    def dmg(self):
        return self.element
    
    #stores last roll performed by the dice
    def setLastRoll(self, theRoll):
        self.lRoll = theRoll
        self.sRolls.append(theRoll)

    def lastRoll(self):
        prevRoll = self.lRoll
        if prevRoll == 0:
            return prevRoll
        else:
            return prevRoll    

    #stores last modifier used by the dice
    def setLastMod(self, theMod):
        self.lastMod = theMod

    def lastMod(self):
        prevMod = self.lastMod
        if prevMod == 0:
            return prevMod
        else:
            return prevMod

    #sets text notification for roll result
    def setResultText(self, text=""):
        self.result = text

    def resultText(self):
        return self.result
    
    #notifies user of the detailed result of the roll
    def rollMessage(self,total, fRoll, sRoll, numSides, mod, weight):
        if weight == 'a':
            self.setResultText("You rolled a {} ({}, {}) on a d{} + {} with advantage.".format(total, fRoll, sRoll, numSides, mod))
        if weight == 'd':
            self.setResultText("You rolled a {} ({}, {}) on a d{} + {} with disadvantage.".format(total, fRoll, sRoll, numSides, mod))
        if weight == 'n':
            self.setResultText("You rolled a {} on a d{} + {}.".format(total, numSides, mod))

    #resets the dice to default values and resets dmg type
    def resetDice(self, type=0):
        self.sRolls = []
        self.lRoll = 0
        self.setDmg(type)  
        self.setResultText("You haven't rolled yet!")
    
    #returns True if last roll was a critical success (20), False if it was a critical failure (1)
    def crit(self):
        if self.lRoll == 1:
            return False

        if self.lRoll == self.side:
            return True
    
    # DICE CREATION
    def d4(self, mod='0', type='0', name='d4'):
        if error_handling.numValidation(mod) == False or error_handling.numValidation(type) == False:
            return "Invalid input. Please enter a number."
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.setName(name)
            self.setSide(4)
            self.resetDice(abs(int(type)))
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
    
    def d6(self, mod='0', type='0', name='d6'):
        if error_handling.numValidation(mod) == False or error_handling.numValidation(type) == False:
            return "Invalid input. Please enter a number."
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.setName(name)
            self.setSide(6)
            self.setMod(mod)
            self.resetDice(type)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
        
    def d8(self, mod='0', dmgType='0', name='d8'):   
        if error_handling.numValidation(mod) == False:
            return "Invalid input. Please enter a number."
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.name = name
            self.setSide(8)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
        
    def d10(self, mod='0', dmgType='0', name='d10'):
        if self.side!= 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.name = name
            self.setSide(10)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)

    def d12(self, mod='0', dmgType='0', name='d12'):
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.name = name
            self.setSide(12)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)

    def d20(self, mod='0', dmgType='0', name='d20'):
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.name = name
            self.setSide(20)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
        
    def d100(self, mod='0', dmgType='0', name='d100'):
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        else:
            self.name = name
            self.setSide(100)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
        
    def custom(self, sides='0', mod='0', dmgType='0', name='new dice'):
        if error_handling.numValidation(sides) == False or error_handling.numValidation(mod) == False:
            return "Invalid input. Please enter a number." 
        if self.side != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.side, self.modifier, self.element)
        elif abs(int(sides)) == 0:
            return "Your custom die must have at least 1 side."
        else:
            self.name = name
            self.setSide(sides)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.side, self.dName, self.modifier, self.element)
    
    # DICE ACTIONS
    
    #def roll(self, die='20'):

    #rolls dice x amount of times
    def rollDice(self, num='1'):
    #input validation
        if error_handling.numValidation(num) == False:
            return "Invalid input. Please use enter a number."
            
        roll = random.randint(1, self.side)
        result = roll + self.mod()
        
        self.rollMessage(result, roll, 0, self.side, self.modifier, 'n')
        return result + self.mod()
    
    #rolls dice with optional adv/disadv, modifier, and number of rolls
    def rollDice(self, weight='n', mod='0', num='1'):
        #input validation
        if error_handling.numValidation(num) == False: 
            return "Invalid input. Please use the format !roll <die> <modifier> <a or d> <# of rolls>."
        if error_handling.weightValidation(weight) == False:
            return "Invalid input. Please use the format !roll <die> <modifier> <a or d> <# of rolls>."
     
        numSides = self.side
        modifier = self.modifier
        dWeight = weight
        
        #roll with advantage
        if dWeight == 'a':
            firstRoll = random.randint(1, numSides)
            secondRoll = random.randint(1, numSides)   
            if firstRoll >= secondRoll:
                result = firstRoll + modifier
            else:
                result = secondRoll + modifier
            self.rollMessage(result, firstRoll, secondRoll, numSides, modifier, dWeight)
            return result
        #roll with disadvantage
        elif dWeight == 'd':
            firstRoll = random.randint(1, numSides)
            secondRoll = random.randint(1, numSides)    
            if firstRoll <= secondRoll:
                    result = firstRoll + modifier
            else:
                    result = secondRoll + modifier
            self.rollMessage(result, firstRoll, secondRoll, numSides, modifier, dWeight)
            return result
        #roll straight
        elif dWeight == 'n':
            diceRoll = random.randint(1, numSides)
            result = diceRoll + self.modifier
            self.rollMessage(result, diceRoll, 0, numSides, modifier, dWeight)
            return result
            
 
    
#SCRAPPED    
    
#rolls multiple dice and adds them together
def multiRoll(numDice):
    if error_handling.numValidation(numDice) == False:
        return "Invalid input. Please enter a number."
    
    dice = []

    #appends dice roll to array
    for i in range(int(numDice)):
        sides = input("Enter the number of sides on die {}: ".format(i + 1))
        modifier = input("Enter the modifier for die {}: ".format(i + 1))
        rolls = input("Enter the number of rolls for die {}: ".format(i + 1))
        #dice.append(rollDmgDice(sides, modifier, rolls))
    
    return sum(dice)