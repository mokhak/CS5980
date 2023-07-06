"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: FIXME
    Created: FIXME
"""

from mugwump import Mugwump
from warrior import Warrior
from die import Die
from character_prot import CharacterProt
"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. Choose local, and it should find it
"""

"""
     # we need to create a Ten-sided die to be used for checking initiative
"""
d10 = Die(10)
def main():  # not testable
    # Local variables
    # Include any variable that will need to be accessed throughout the program here

    # sentinel value for the game loop
    keep_playing = True

    # String used to determine the winner of the epic battle
    victor = ""
    # game loop


    while keep_playing:
        # print the introduction and rules
        intro()
        
        print( "Would you like Mugwump to be AI or Player Controlled?" 
            "\nEnter 1 for AI, 2 for Player")
        
        mugwump_play = input()
        
        print( "Would you like Warrior to be AI or Player Controlled?" 
            "\nEnter 1 for AI, 2 for Player")
        
        warrior_play = input()
        

        # initialize game
        # Initialize the Warrior and Mugwump classes, set the current victor to "none"
        # change to player1 and player2, we ask the user what is what
        if(mugwump_play == "1"):
            mugwump = Mugwump(True)
        else:
            mugwump = Mugwump(False)
            
        if(warrior_play == "1"):
            warrior = Warrior(True)
        else:
            warrior = Warrior(False)
            
        # if you decide to use a Protocol, asset isinstance right here
        assert isinstance(warrior, CharacterProt)
        assert isinstance(mugwump, CharacterProt)
        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(warrior, mugwump)
            victor = battle(warrior, mugwump)

        # declare the winner
            if (victor != "none"): # one of them has won
                report(warrior, mugwump)
                victory(victor)
                # ask to play again
                keep_playing = playAgain()


    # Thank the user for playing your game
    print("Thank you for playing Battle Simulator 3000!")


"""
   This method displays the introduction to the game and gives a description of the rules.
 """
def intro():  # not testable
    # Write a suitable introduction to your game
    print(  "Welcome to Battle Simulator 3000! The world's more low tech battle simulator!"
            "You are a Valiant Warrior defending your humble village from an evil Mugwump! Fight bravely, "
            "or the citizens of your town will be the Mugwump's dinner!"
            "\nYou have your Trusty Sword, which deals decent damage, but can be tough to hit with sometimes. "
            "You also have your Shield of Light, which is not as strong as your sword, but is easier to deal "
            "damage with."
            "\nLet the epic battle begin!")
    


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
 """
def battle(warrior, mugwump):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative() # this a 1 or 2
    # attack code
    # If the Warrior attacks first
    if (cur_inititive == 1):
        # Warrior attacks and assigns the resulting damage to the mugwump
        print("The warrior attacks first!")
        
        if(warrior.aiController == True):
            cur_attack = 0
        else:
            cur_attack = attackChoice()
        damage = warrior.attack((cur_attack)) #calculate damage caused by warrior

        mugwump.takeDamage(damage) # apply damage to mugwump
        # Check if the Mugwump has been defeated
        if (mugwump.hitPoints <= 0):
            return "warrior"
        
        # If not, Mugwump attacks!
        
        if(mugwump.aiController == True):
            cur_attack = 0
        else:
            cur_attack = attackChoice()
            
        damage = mugwump.attack(cur_attack)
        
        # the mugwump may have healed itself, so have to check
        if(damage > 0):
            warrior.takeDamage(damage)
        else:  #mugwump healed
            mugwump.takeDamage(damage) #healing because it is negative

        if (warrior.hitPoints == 0):
            return "mugwump"  #mugwump wins!
    else: # mugwump attacks first!
        print("The mugwump attacks first!")
        # mugwump attacks and assigns the resulting damage to the warrior
        if(mugwump.aiController == True):
            cur_attack = 0
        else:
            cur_attack = attackChoice()
            
        damage = mugwump.attack(cur_attack)
        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            warrior.takeDamage(damage)
        else:  # mugwump healed
            mugwump.takeDamage(damage)  # healing because it is negative

        if (warrior.hitPoints == 0):
            return "mugwump"  # mugwump wins!

        if(mugwump.aiController == True):
            cur_attack = 0
        else:
            cur_attack = attackChoice()
        damage = warrior.attack(cur_attack)  # calculate damage caused by warrior

        mugwump.takeDamage(damage)  # apply damage to mugwump
        # Check if the Mugwump has been defeated
        if (mugwump.hitPoints <= 0):
            return "warrior"


    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """
def report(warrior, mugwump):  # not testable
    print(f"Warrior HP: {warrior.hitPoints}")
    print(f"Mugwump HP: {mugwump.hitPoints}")




"""
   This method asks the user what attack type they want to use and returns the result
   @return 1 for sword, 2 for shield
 """
def attackChoice() -> int: # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    # this may need to change, probably needs to move into mugwump and warrior
    # mugwump already has ai, but when controlled human will need something like this

    choice = int(input( "How would you like to attack?\n"
                        "1. Your Trusty Sword\n"
                        "2. Your Shield of Light\n"
                        "Enter choice: "))
    return choice


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if the mugwump goes first
 """
# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int: # return 1 for warrior, 2 for mugwump
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    warrior_initiative = d10.roll()
    mugwump_inititive = d10.roll()
    while (warrior_initiative == mugwump_inititive):
        warrior_initiative = d10.roll()
        mugwump_inititive = d10.roll()

    if (warrior_initiative > mugwump_inititive):
        return 1  # warrior goes first
    else:
        return 2  # mugwump goes first



"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """
def victory(victor):  # not testable (or at least we won't worry about testing it)
    if (victor == "warrior"):
        print(  "The citizens cheer and invite you back to town for a feast"
                " as thanks for saving their lives (again)!")
    else:
        print("You loose to the Mugwump! He mocks you for how pathetically you fought")



"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """
def playAgain() -> bool:  # this should be testable, see https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    choice = input("Would you like to play again (yes/no)?")
    if (str.lower(choice) == "y" or str.lower(choice)  == "yes"):
        return True
    return False

if __name__ == "__main__":
    main()