from diceSimulate import Dice
dice = Dice()

class Stats:
    def __init__(self):
        self.mainStats = {"Strength":0, "Dexterity":0, "Constitution":0,"Intelligence":0, "Wisdom":0,"Charisma":0}
    def roll_type_one(self):
        def stat_roll():
            #roll d6 take highest 3 numbers and add them
            rolls = []
            for item in range(0,4):
                rolls.append(dice.d6())
            rolls = sorted(rolls)
            for item in range(0,1):
                rolls.pop(item)
            total = rolls[0]+rolls[1]+rolls[2]
            return total
        for item in self.mainStats:
            self.mainStats[item]=stat_roll()
    def default_stats(self):
        defaultStats = [15,14,13,12,10,8]
        def choose(a):
            while True:
                    if len(a) == 1:
                        #if all but one value has been chosen, set the last value to the last ability score.
                        return int(a[0])
                    else:
                        try:
                            #ask for one of the stats
                            print(a)
                            answer = input("Please enter your answer: " )
                            if int(answer) not in a:
                                print("Sorry, Choose from the remaining numbers.", a)
                                #better try again... Return to the start of the loop
                                continue
                            else:
                                return int(answer)
                                break
                        except ValueError:
                            print("Error from input")
                            pass
        #loop through the main stats(ability scores) to choose between the default values.
        for item in self.mainStats:
            print("Rolling for ", item)
            #set default choice to variable.
            defstat = choose(defaultStats)
            #set the default number to your ability score.
            self.mainStats[item] = defstat
            #once the choice is made, remove the number from the remaining options.
            defaultStats.remove(defstat)
    def display_stats(self):
        return self.mainStats


stats = Stats()
print(stats.roll_type_one())
#stats.default_stats()
print(stats.display_stats())
"""
Roll your ability scores. You have 6 Ability scores to roll for:
Strength, Dexterity, Constitution, Intellect, and Wisdom.
You can either roll 4 6-sided die and record the cumulative total of the highest 3 dice 6 times or
take the "standard set" which is 15,14,13,12,10,8.
"""
