#Barbarian (Bbn)
#Bard (Brd)
#Cleric (Clr)
#Druid (Drd)
#Fighter (Ftr)
#Monk (Mnk)
#Paladin (Pal)
#Ranger (Rgr)
#Rogue (Rog)
#Sorcerer (Sor)
#Wizard (Wiz)
class dndClass:
    def __init__(self,pclass,level):
        '''
        Hit Points
        Hit Dice: 1d12 per barbarian level
        Hit Points at 1st Level: 12 + your Constitution modifier
        Hit Points at Higher Levels: 1d12 (or 7) + your Constitution modifier per barbarian level after 1st
        '''
        self.hit_dice = str(level) + "d12"
        self.classify = pclass
        self.level = level
    def level_stats(self):
        #print(self.hit_dice)
        if self.level >= 17 and self.level <21:
            #Levels 17-20
            #proficiencies = 2
            #rages = 2
            #rage_damage = 2
            #print("this character is between level 17 and 20")
            return "level: " + str(self.level)
        elif self.level < 17  and self.level >= 13:
            #Levels 13-17
            #proficiencies = 2
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 13")
            return "level: " + str(self.level)
        elif self.level < 13 and self.level >= 9:
            #Levels 9-12
            #proficiencies = 2
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 9")
            return "level: " + str(self.level)
        elif self.level < 9 and self.level >= 5:
            #Levels 5-9
            #proficiencies = 2
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 5")
            return "level: " + str(self.level)
        elif self.level < 4:
            #Levels 1-4
            #print("this character is at least lvl 1")
            return "level: " + str(self.level)
        else:
            #print("This character is supremely weak or is a god. This level is invalid")
            return "level: " + str(self.level)

    def classInfo(self):
        return self.hit_dice, self.classify, self.level
barbarian = dndClass("Barbarian",17)
barbarian.level_stats()
print(barbarian.classInfo())
