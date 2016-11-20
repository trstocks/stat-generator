import random
'''
min = 1
max = 20

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")
'''
class Dice:
    def d20(self):
        return random.randint(1,20)
    def d12(self):
        return random.randint(1,12)
    def d10(self):
        return random.randint(1,10)
    def d8(self):
        return random.randint(1,8)
    def d6(self):
        return random.randint(1,6)
    def d4(self):
        return random.randint(1,4)
#dice1 = Dice()
#dice1.d20()
#dice1.d12()
