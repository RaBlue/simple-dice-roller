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
        self.sides = abs(int(die))
        self.modifier = int(modifier)
        self.dmgType = ['none', 'bludgeoning', 'piercing', 'slashing', 'fire', 'cold', 'lightning', 'thunder', 'acid', 'poison']
        self.element = self.dmgType[0]
        self.lRoll = 0
        self.lMod = 0
        self.sRolls = []

    # DICE CREATION
    def setName(self, name):
        self.dName = name

    def name(self):
        return self.dName

    def setSide(self, sides):
        if error_handling.numValidation(sides) == False:
            return "Invalid input. Please enter a number."
        self.sides = abs(int(sides))

    def sides(self):        
        return self.sides

    def setMod(self, modifier):
        if error_handling.numValidation(modifier) == False:
            return "Invalid input. Please use the format !roll <die> <modifier>."
        self.modifier = modifier
    
    def mod(self):
        return self.modifier    

    def setDmg(self, type=0):
        self.element = self.dmgType[type]

    def dmg(self):
        return self.element
    
    def lastRoll(self):
        prevRoll = self.lRoll
        if prevRoll == 0:
            return prevRoll
        else:
            return prevRoll    

    def setLastRoll(self, theRoll):
        self.lRoll = theRoll
        self.sRolls.append(theRoll)

    def lastMod(self):
        prevMod = self.lastMod
        if prevMod == 0:
            return prevMod
        else:
            return prevMod

    def setLastMod(self, theMod):
        self.lastMod = theMod

    def resetDice(self, type=0):
        self.sRolls = []
        self.lRoll = 0
        self.element = self.dmgType[type]  
    
    def d4(self, mod='0', type='0', name='new dice'):
        if error_handling.numValidation(mod) == False or error_handling.numValidation(type) == False:
            return "Invalid input. Please enter a number."
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.mod(), self.dmg())
        else:
            self.setName(name)
            self.setSide(4)
            self.setMod(mod)
            self.resetDice(abs(int(type)))
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name(), self.mod(), self.dmg())
    
    def d6(self, mod='0', type='0', name='new dice'):
        if error_handling.numValidation(mod) == False or error_handling.numValidation(type) == False:
            return "Invalid input. Please enter a number."
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType)
        else:
            self.setName(name)
            self.setSide(6)
            self.setMod(mod)
            self.resetDice(type)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())
        
    def d8(self, mod='0', dmgType='none', name='new dice'):   
        if error_handling.numValidation(mod) == False:
            return "Invalid input. Please enter a number."
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        else:
            self.name = name
            self.setSide(8)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())
        
    def d10(self, mod='0', dmgType='none', name='new dice'):
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        else:
            self.name = name
            self.setSide(10)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())

    def d12(self, mod='0', dmgType='none', name='new dice'):
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        else:
            self.name = name
            self.setSide(12)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())

    def d20(self, mod='0', dmgType='none', name='new dice'):
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        else:
            self.name = name
            self.setSide(20)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())
        
    def d100(self, mod='0', dmgType='none', name='new dice'):
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        else:
            self.name = name
            self.setSide(100)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())
        
    def custom(self, sides='0', mod='0', dmgType='none', name='new dice'):
        if error_handling.numValidation(sides) == False or error_handling.numValidation(mod) == False:
            return "Invalid input. Please enter a number." 
        if self.sides() != 0:
            return "You have already created this die. It is a d{} with a modifier of {} and a damage type of {}.".format(self.sides(), self.modifier(), self.dmgType())
        elif abs(int(sides)) == 0:
            return "Your custom die must have at least 1 side."
        else:
            self.name = name
            self.setSide(sides)
            self.setMod(mod)
            self.resetDice(dmgType)
            return "You've created a new d{} named {} with a modifier of {} and a damage type of {}.".format(self.sides(), self.name, self.modifier(), self.dmgType())
    
    # DICE ACTIONS
    
    def rollDice(self, num='1'):
    #rolls damage die x times and returns total value
    #input validation
        if error_handling.numValidation(num) == False:
            return "Invalid input. Please use enter a number."
            
        rolls = abs(int(num))
        result = 0
        
        #roll one damage die i amount of times and add to total
        for i in rolls:
            roll = random.randint(1, self.sides)
            result += roll

        return result + self.modifier
    
    def rollDice(self, weight='none', num='1'):
    #rolls the die based on input sides and modifier and sends the result
        #input validation
        if error_handling.numValidation(num) == False: 
            return "Invalid input. Please use the format !roll <die> <modifier> <a or d> <# of rolls>."
        if error_handling.weightValidation(weight) == False:
            return "Invalid input. Please use the format !roll <die> <modifier> <a or d> <# of rolls>."
     
        numSides = self.sides()
        mod = self.modifier()
        dWeight = weight
        roll = abs(int(num))
        total = []
        
        for i in roll:
            #roll with advantage
            if dWeight == 'a':
                firstRoll = random.randint(1, numSides)
                secondRoll = random.randint(1, numSides)    
                if firstRoll >= secondRoll:
                    result = firstRoll + mod
                else:
                    result = secondRoll + mod
                total.append(result)
                #return critRoll(result, numSides, mod) + "\nAdvantage! You rolled a {} ({}, {}) on a d{} with a modifier of {}.".format(result, firstRoll, secondRoll, numSides, mod)
            #roll with disadvantage
            elif dWeight == 'd':
                firstRoll = random.randint(1, numSides)
                secondRoll = random.randint(1, numSides)    
                if firstRoll <= secondRoll:
                        result = firstRoll + mod
                else:
                        result = secondRoll + mod
                total.append(result)
                #return critRoll(result, numSides, mod) + "\nDisadvantage! You rolled a {} ({}, {}) on a d{} with a modifier of {}.".format(result, firstRoll, secondRoll, numSides, mod)
            #roll straight
            elif dWeight == 'none':
                result = random.randint(1, numSides) + mod
                total.append(result)
                #return critRoll(result, numSides, mod) + "\nYou rolled a {} on a d{} with a modifier of {}.".format(result, numSides, mod)
                #error message for invalid input
        return sum(total)
   
def crit(self):
#returns statement based on critical rolls
    modifier = self.mod()
    die = self.sides()
    #natural 1
    if self.lastRoll() == 1:
        return False

    #natural 20
    if self.lastRoll() == self.sides():
        return True


#PROBABLY NOT USE THESE
    
def rollMessage(result, fRoll, sRoll, numSides, mod, weight):
    if weight == 'a':
        return "You rolled a {} ({}, {}) on a d{} + {} with advantage.".format(result, fRoll, sRoll, numSides, mod)
    if weight == 'd':
        return "You rolled a {} ({}, {}) on a d{} + {} with disadvantage.".format(result, fRoll, sRoll, numSides, mod)
    if weight == 'none':
        return "You rolled a {} on a d{} + {}.".format(result, numSides, mod)
    
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