'''
Experience Points	Level	Proficiency Bonus
    0                1	          +2
    300	             2	          +2
    900	             3            +2
    2,700	         4	          +2
    6,500            5	          +3
    14,000           6            +3
    23,000	         7	          +3
    34,000	         8	          +3
    48,000	         9	          +3
    64,000	         10	          +3
    85,000	         11	          +4
    100,000	         12	          +4
    120,000	         13	          +5
    140,000	         14	          +5
    165,000	         15	          +5
    195,000	         16	          +5
    225,000	         17	          +6
    265,000	         18	          +6
    305,000	         19	          +6
    355,000	         20	          +6
'''
class Level:
    levelxp = {1:0,2:200,3:900,4:2700,5:6500,6:14000,7:23000,8:34000, 9:48000,10:64000,11:85000, +
                12:100000,13:120000,14:140000,15:165000,16:195000,17:225000,18:265000,19:305000,20:355000}

    def __init__(self,level):
        self.level = level
    def proficiencyBonus(self):
        #print(self.hit_dice)

        if self.level >= 17 and self.level <21:

            #Levels 17-20
            #proficiencies = 2
            print("Proficiency Bonus is +6")
            #rages = 2
            #rage_damage = 2
            #print("this character is between level 17 and 20")
            return "level: " + str(self.level)
        elif self.level < 17  and self.level >= 13:
            #Levels 13-17
            #proficiencies = 2
            print("Proficiency Bonus is +5")
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 13")
            return "level: " + str(self.level)
        elif self.level < 13 and self.level >= 9:
            #Levels 9-12
            #proficiencies = 2
            print("Proficiency Bonus is +4")
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 9")
            return "level: " + str(self.level)
        elif self.level < 9 and self.level >= 5:
            #Levels 5-9
            #proficiencies = 2
            print("Proficiency Bonus is +3")
            #rages = 2
            #rage_damage = 2
            #print("this character is at least lvl 5")
            return "level: " + str(self.level)
        elif self.level < 4:
            #Levels 1-4
            #print("this character is at least lvl 1")
            print("Proficiency Bonus is +2")
            return "level: " + str(self.level)
        else:
            #print("This character is supremely weak or is a god. This level is invalid")
            return "level: " + str(self.level)
    def addExperience(self,exp,addExp):
        self.experience = exp + addExp
        for item in Level.levelxp:
            if self.experience > Level.levelxp[item] and exp < Level.levelxp[item]:
                self.level = item


    def dislayLevelInfo(self):
        print("Level: ", self.level)


mylevel=Level(7)
mylevel.proficiencyBonus()
mylevel.addExperience(300,620)
mylevel.dislayLevelInfo()
