'''
Basics:
Character Name
Class & Level
Background
Player name
Faction
Race
Alignment
Experience Points
DCI number
'''
from diceSimulate import Dice
dice = Dice()
class Player:
    plevel = 0
    def __init__(self, pname, pclass, prace, owner):
        self.pname = pname
        self.pclass = pclass
        self.prace = prace
        self.owner = owner
        self.pstats = {'Strength': 0,'Dexterity': 0,'Constitution': 0,'Intelligence': 0,'Wisdom': 0, "Charisma":0 }


    def main_stats(self):
        #Strength,Dexterity,Constitution,Intelligence,Wisdom
        #Player.plevel += 1
        for s in self.pstats:
            self.pstats[s] = dice.d20()

        return self.pstats


    def displayPlayer(self):
        print ("Name : ", self.pname,  ", Class: ", self.pclass, ", Race: ", self.prace)
        print(self.pstats)




pl1 = Player("Cera", "Bard", "Elf" , "Troy")
pl2 = Player("OstrichKing", "Barbarian", "Human" , "Troy")
#pl1.displayPlayer()
#print pl1.main_stats()
for i in pl1.pstats.items():
    if i[1] == 0:
        pl1.main_stats()
    else:
        break
pl1.displayPlayer()
pl1.displayPlayer()
with open(pl1.pname+"Character.txt", "w") as text_file:
    text_file.write("Stats - {0}".format(pl1.displayPlayer()))



'''
Experience Tracking, Level, Proficiency Bonus

'''
