"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: Eliana Biggers & Kirat Mokha
    Created: 7/13/23
"""

from character import Mugwump, Warrior
from eliana_char import Dragon
from die2 import Die
from character_prot import CharacterProt
import color
from kirat_char import Edith
import tkinter
from tkinter import filedialog
import json

"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. 
 Choose local, and it should find it
"""

# Create a Ten-sided die to be used for checking initiative
d10 = Die(10)


def main():
    
    # Local variables
    
    # sentinel value for the game loop
    keep_playing = True

    # String used to determine the winner of the epic battle
    victor = ""

    # game loop
    while keep_playing:
        # print the introduction and rules
        intro()

        # chooseCharacters assigns character objects to player1 and player2
        player1, player2 = chooseCharacters()
        
        # making sure that characters adhere to the Character Protocol specified
        assert isinstance(player1, CharacterProt)
        assert isinstance(player2, CharacterProt)

        # Set the current victor to "none"
        victor = "none"

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(player1, player2)
            victor = battle(player1, player2)

        # declare the winner
            if victor != "none":  # one of them has won
                report(player1, player2)
                victory(victor)
                # Thank the user for playing your game
                print(f"{color.BOLD}Thank you for playing Battle Simulator 3000!\n{color.END}")

                saveChar(player1, player2)  # ask to save character stats
                # ask to play again
                keep_playing = playAgain()


# This method displays the introduction to the game and gives a description of the rules.
def intro():
    print("\nWelcome to Battle Simulator 3000! The world's more low tech battle simulator!"
            "\nYou can choose to be a Valiant Warrior, Evil Mugwump, Vicious Dragon or Cranky Old Lady Edith Burton!"
            "\nThe Dragon and Edith have special attacks that can be unlocked as the game is played."
            "\nThe Mugwump, Dragon, and Edith have the ability to heal for a small amount of HP.\n"
            f"{color.BOLD}\nLet the epic battle begin!\n{color.END}")


# This method asks the user to choose a character for player 1 and player 2
# player 1 and player 2 are then assigned characters from the abstract class Character and returned
def chooseCharacters():
    # Prompt user for character choices and computer options
    player1_choice = input("Choose a character for player 1\n"
                           "1. Warrior\n"
                           "2. Mugwump\n"
                           "3. Dragon\n"
                           "4. Edith\n"
                           "5. Load a character\n"
                           "Enter your choice: ")

    # Create player and computer objects based on user choices
    if player1_choice == "1":
        player1 = Warrior(is_computer=False)  # player 1 will always be player controlled

    elif player1_choice == "2":
        player1 = Mugwump(is_computer=False)

    elif player1_choice == "3":
        player1 = Dragon(is_computer=False)

    elif player1_choice == "4":
        player1 = Edith(is_computer=False)
        
    elif player1_choice == "5": # load a .json file with the character user saved previously
        player1 = LoadFile(False)

    else:
        print("Invalid player 1 character choice. Defaulting to Warrior.")
        player1 = Warrior(is_computer=False)

    # Player 2 character choice AND computer controlled choice
    player2_choice = input("Choose a character for player 2\n"
                           "1. Warrior\n"
                           "2. Mugwump\n"
                           "3. Dragon\n"
                           "4. Edith \n"
                           "5. Load a character\n"
                           "Enter your choice: ")

    computer_choice = input("Will player 2 be computer controlled? (Enter yes or no): ")

    if player2_choice == "1":  # Warrior

        if str.lower(computer_choice) == "n" or str.lower(computer_choice) == "no":
            player2 = Warrior(is_computer=False)  # Player 2 is player controlled warrior
        elif str.lower(computer_choice) == "y" or str.lower(computer_choice) == "yes":
            player2 = Warrior(is_computer=True)  # Player 2 is computer controlled warrior
        else:
            print("Invalid entry. Player 2 defaulted to computer player")
            player2 = Warrior(is_computer=True)

    elif player2_choice == "2":  # mugwump

        if str.lower(computer_choice) == "n" or str.lower(computer_choice) == "no":
            player2 = Mugwump(is_computer=False)  # Player 2 is player controlled mugwump
        elif str.lower(computer_choice) == "y" or str.lower(computer_choice) == "yes":
            player2 = Mugwump(is_computer=True)  # Player 2 is computer controlled mugwump
        else:
            print("Invalid entry. Player 2 defaulted to computer player")
            player2 = Mugwump(is_computer=True)

    elif player2_choice == "3":  # dragon

        if str.lower(computer_choice) == "n" or str.lower(computer_choice) == "no":
            player2 = Dragon(is_computer=False)  # Player 2 is player controlled dragon
        elif str.lower(computer_choice) == "y" or str.lower(computer_choice) == "yes":
            player2 = Dragon(is_computer=True)  # Player 2 is computer controlled dragon
        else:
            print("Invalid entry. Player 2 defaulted to computer player")
            player2 = Dragon(is_computer=True)

    elif player2_choice == "4":  # Edith
        if str.lower(computer_choice) == "n" or str.lower(computer_choice) == "no":
            player2 = Edith(is_computer=False)  # Player 2 is player controlled dragon
        elif str.lower(computer_choice) == "y" or str.lower(computer_choice) == "yes":
            player2 = Edith(is_computer=True)  # Player 2 is computer controlled dragon
        else:
            print("Invalid entry. Player 2 defaulted to computer player")
            player2 = Edith(is_computer=True)
            
    elif player2_choice == "5":  # Load Character
        if str.lower(computer_choice) == "n" or str.lower(computer_choice) == "no":
            player2 = LoadFile(False)
        elif str.lower(computer_choice) == "y" or str.lower(computer_choice) == "yes":
            player2 = LoadFile(True)
        else:
            print("Invalid entry. Player 2 defaulted to computer player")
            player2 = LoadFile(True)

    else:
        print("Invalid player 2 entries. Defaulting to computer controlled Mugwump.")
        player2 = Mugwump(is_computer=True)  # default is computer controlled mugwump

    return player1, player2


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
"""


def battle(player1, player2):
    # determine who attacks first and store the result
    cur_initiative = initiative()  # this a 1 or 2

    # attack code
    # If player1 attacks first
    if cur_initiative == 1:
        # Player 1 attacks and assigns the resulting damage to player 2
        print("Player 1 attacks!")
        damage = player1.attack()  # calculate damage caused by player 1
        # Check for heal...
        if damage > 0:
            player2.takeDamage(damage)
        else:
            player1.takeDamage(damage)

        # Check if player2 has been defeated
        if player2.hitPoints <= 0:
            return "player 1"

        # If not, player2 attacks
        print("Player 2 attacks!")
        damage = player2.attack()

        # Check for heal...
        if damage > 0:
            player1.takeDamage(damage)
        else:
            player2.takeDamage(damage)

        if player1.hitPoints == 0:
            return "player 2"  # Player 2 wins

    else:  # player 2 attacks first
        print("Player 2 attacks!")
        # player 2 attacks and assigns the resulting damage
        damage = player2.attack()

        #  Check for heal...
        if damage > 0:
            player1.takeDamage(damage)
        else:
            player2.takeDamage(damage)

        if player1.hitPoints == 0:
            return "player 2"  # Player 2 wins

        damage = player1.attack()  # calculate damage caused by player 1
        #  Check for heal...
        if damage > 0:
            player2.takeDamage(damage)
        else:
            player1.takeDamage(damage)

        # Check if the player 2 has been defeated
        if player2.hitPoints <= 0:
            return "player 1"

    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """


def report(player1, player2):
    print(f"Player 1 HP: {player1.hitPoints}")
    print(f"Player 2 HP: {player2.hitPoints}\n")


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if player 1 goes first, 2 if player 2 goes first
"""


def initiative() -> int:  # return 1 for player 1, 2 for player 2
    # roll for initiative for both combatants
    # until one initiative is greater than the other
    player1_initiative = d10.roll()
    player2_initiative = d10.roll()

    while player1_initiative == player2_initiative:
        player1_initiative = d10.roll()
        player2_initiative = d10.roll()

    if player1_initiative > player2_initiative:
        return 1  # player1 goes first
    else:
        return 2  # player2 goes first


"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
"""


def victory(victor):
    if victor == "player 1":
        print(f"{color.CYAN}Player 1 has won this round!\n{color.END}")
    else:  # victor is player 2
        print(f"{color.PURPLE}Player 2 has won this round!\n{color.END}")


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """


def playAgain() -> bool:
    choice = input("Would you like to play again (yes/no)?")
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        return True
    return False

"""
    This method asks the user if they would like to save one of the characters
    from their most recent game. It also calls SaveFile method.
    @param in player1, player2 classes
"""

def saveChar(player1, player2):
    player_1 = False  # keep track of which player has been saved
    player_2 = False
    
    player1_char = player1.nickname # save the default nick name of the players to identify what class they are
    player2_char = player2.nickname

    choice = input("Would you like to save your character stats? (yes or no): ") # ask the use if and which character they would like to save
    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        player = input("Which player would you like to save? (1 or 2): ")
        if player == "1":
            player1.nickname = input("Enter a nickname for player 1's character: ") # ask user to give character a nick name
            player_1 = True
            
            p1_data = { # create python dict with character stats
                'character': player1_char,
                'nickname': player1.nickname,
                'maxHitPoints': player1.maxHitPoints
            }
            
            SaveFile(p1_data) # call SaveFile method to save .json file
            
        elif player == "2":
            player2.nickname = input("Enter a nickname for player 2's character: ")
            player_2 = True
            
            p2_data = {
                'character': player2_char,
                'nickname': player2.nickname,
                'maxHitPoints': player2.maxHitPoints
            }
            
            SaveFile(p2_data)
            
        else:
            print("Invalid player entry")
    else:
        pass

    if str.lower(choice) == "y" or str.lower(choice) == "yes":
        choice2 = input("Would you like to save the stats for another character? (yes or no): ")
        if str.lower(choice2) == "y" or str.lower(choice2) == "yes":
            if not player_1:  # if player 1 has not been saved yet
                player1.nickname = input("Enter a nickname for player 1's character: ")
                
                p1_data = {
                    'character': player1_char,
                    'nickname': player1.nickname,
                    'maxHitPoints': player1.maxHitPoints
                }
                
                SaveFile(p1_data)
                
            elif not player_2:  # if player 2 has not been saved yet
                player2.nickname = input("Enter a nickname for player 2's character: ")
                
                p2_data = {
                    'character': player2_char,
                    'nickname': player2.nickname,
                    'maxHitPoints': player2.maxHitPoints
                }
                
                SaveFile(p2_data)
        else:
            pass

""" 
    This method asks the user to specify the location where they would
    like to save their character and then saves a .json file at that 
    location. 
    @params in player stats as python dict
"""
def SaveFile(player_data):
    tkinter.Tk().withdraw() # using tkinter library open a dialogue box for user to specify saving location
    player = filedialog.asksaveasfilename(initialfile=f"{player_data.get('nickname')}.json",defaultextension=".json")
    with open(player, "w") as json_file: # save and write .json file with dict
        json.dump(player_data,json_file)
        
        
        
"""
    This method allows the user to load in a previously saved character.
    Once the file is loaded, the method creates the character object
    with the respective class.
    @params in computer control enabled
    @return character object
"""
def LoadFile(computerControlled):
    tkinter.Tk().withdraw() # using tkinter library open dialogue box for user to specify character file
    charFile = filedialog.askopenfilename(defaultextension=".json")
    with open(charFile, 'r') as file:
        data = json.load(file) # load the .json file
        
    print(f"Loading {data['nickname']} as {data['character']}...")
    
    match data['character']: # create character object with the respective class specified in .json file
        case 'Warrior':
            player = Warrior(computerControlled)
        case 'Mugwump':
            player = Mugwump(computerControlled)
        case 'Dragon':
            player = Dragon(computerControlled)
        case 'Edith':
            player = Edith(computerControlled)
    
    # put in parameter for .json file into the character object        
    player.nickname = data['nickname']
    player.maxHitPoints = data['maxHitPoints']
    
    # print out character information
    print(f"Successfully loaded {data['character']} with nickname {data['nickname']} and {data['maxHitPoints']} hit points.")
    
    # return the character object
    return player
    

if __name__ == "__main__":
    main()
