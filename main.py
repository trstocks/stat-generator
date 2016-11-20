#get basic character information
from player import Player
pl1 = Player
def main():
    #Character Name
    charname = input("What do you want to name your character? ")
    #Class & Level
    charclass = input("Please choose your character\'s class: \n a. Bard b. barbarian" )
    charlvl = input("Choose a starting level:")
    #Background
    boolbgc = input("Do you want a Background character?(y/n): ")
    if boolbgc == 'y' or boolbgc == 'Y':
        charbackground = input("tell me your story: ")
    #Player name
    playername = input("Enter the owner of this character: ")
    #Faction
    #charfaction = input("Choose your faction: ")
    #Race
    charrace = input("Choose race: \n a. Human b. Elf c. Half-Elf")
    #Alignment
    charalignment = input("Choose Alignment:\n 1. Lawful good (LG)\n2. Neutral good (NG)\n3. Chaotic good (CG)\n" +
                            "4. Lawful neutral (LN) \n 5. Neutral (LN)\n6. Chaotic neutral (CN)\n7. Lawful evil (LE)\n" +
                            "8. Neutral evil (NE)\n9. haotic evil (CE)")

    pl1(charname,charclass, charrace, playername)
    #pl1.displayPlayer()
    print(alignment(charalignment))

def alignment(input):
    if input == "1":
        print("Lawful good (LG) creatures can be counted on to do the right thing as expected by society. Gold Dragons, paladins, and most dwarves are lawful good.")
    elif input == "2":
        print("Neutral good (NG) folk do the best they can to help others according to their needs. Many Celestials, some Cloud Giants, and most gnomes are neutral good.")
    elif input == "3":
        print("Chaotic good (CG) creatures act as their conscience directs, with little regard for what others expect. Copper Dragons, many elves, and unicorns are chaotic good.")
    elif input == "4":
        print("Lawful neutral (LN) individuals act in accordance with law, tradition, or personal codes. Many monks and some wizards are lawful neutral.")
    elif input == "5":
        print("Neutral (N) is the alignment of those who prefer to steer clear of moral questions and don’t take sides, doing what seems best at the time. Lizardfolk, most druids, and many humans are neutral.")
    elif input == "6":
        print("Chaotic neutral (CN) creatures follow their whims, holding their personal freedom above all else. Many barbarians and rogues, and some bards, are chaotic neutral.")
    elif input == "7":
        print("Lawful evil (LE) creatures methodically take what they want, within the limits of a code of tradition, loyalty, or order. Devils, blue Dragons, and Hobgoblins are lawful evil.")
    elif input == "8":
        print("Neutral evil (NE) is the alignment of those who do whatever they can get away with, without compassion or qualms. Many drow, some Cloud Giants, and Goblins are neutral evil.")
    elif input == "9":
        print("Chaotic evil (CE) creatures act with arbitrary violence, spurred by their greed, Hatred, or bloodlust. Demons, red Dragons, and orcs are chaotic evil.")
    else:
        print("This alignment is irrelevent")

main()
