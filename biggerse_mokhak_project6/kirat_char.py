# Character Properties: Edith Burton
#   Attacks:
#       Cane Throw - Deals less damage but hits more often
#       Walker Shove - Deals more damage but hits less often
#   Heals:
#       Pop an Advil - Heals by popping an Advil
#   Special Attack:
#       Verbal Abuse - If you hit for 7 points or more, you can verbally abuse your opponent for a large amount of emotional damage

from die2 import Die
import color

class Edith:
    def __init__(self, is_computer):
        self.nickname = 'Edith'
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)
        self.numHits = 0
        
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
        self.is_computer = is_computer
        self.enable_sp_attack = False
        
    def attack(self):
        damage = 0
        
        if(self.is_computer == False):
            
            if(self.enable_sp_attack == True):
                
                sp_userInput = input("Would you like to verbally abuse your opponent? (yes/no): ")
                if(str.lower(sp_userInput) == "y" or str.lower(sp_userInput) == "yes"):
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll() + self.d6.roll()
                    print(f"{color.GREEN}You caused damage amounting to {damage}\n{color.END}")
                else:
                    print("You're too nice!")
                self.enable_sp_attack = False
                
            else:
                attack_type = int(input("How would you like to attack?\n"
                                        "1. Cane Throw\n"
                                        "2. Walker Shove\n"
                                        "3. Pop an Advil\n"
                                        "Enter choice: "))
                match attack_type:
                    case 1:
                        if self.d20.roll() >= 10:
                            damage = self.d6.roll() + self.d6.roll()
                            print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                        else:
                            print(f"{color.RED}You miss!{color.END}")
                            
                    case 2:
                        if self.d20.roll() >=15:
                            damage = self.d6.roll() + self.d6.roll() + self.d6.roll()
                            print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                        else:
                            print(f"{color.RED}You miss!{color.END}")   
                            
                    case 3:
                        damage = -1 * self.d6.roll()
                        print(f"{color.GREEN}You heal for {-1 * damage}\n{color.END}")
                        
                if(damage >= 7):
                    self.enable_sp_attack = True
            
        elif(self.is_computer == True):
            damage = 0
            
            if(self.enable_sp_attack == True):
                sp_roll = self.ai(self.enable_sp_attack)
                match sp_roll:
                    case "yes":
                        damage = self.d6.roll() + self.d6.roll() + self.d6.roll() + self.d6.roll()
                        print(f"{color.GREEN}Edith caused damage amounting to {damage}\n{color.END}")
                    case "no":
                        print("Edith spares you!")
                self.enable_sp_attack = False
            
            else:   
                attack_type = self.ai(self.enable_sp_attack)
                
                match attack_type:
                    case 1:
                        if self.d20.roll() >= 10:
                            damage = self.d6.roll() + self.d6.roll()
                            print(f"{color.GREEN}Edith hit for {damage}\n{color.END}")
                        else:
                            print(f"{color.RED}Edith missed!{color.END}")
                            
                    case 2:
                        if self.d20.roll() >=15:
                            damage = self.d6.roll() + self.d6.roll() + self.d6.roll()
                            print(f"{color.GREEN}Edith hit for {damage}\n{color.END}")
                        else:
                            print(f"{color.RED}Edith missed!{color.END}")   
                            
                    case 3:
                        damage = -1 * self.d6.roll()
                        print(f"{color.GREEN}Edith heals for {-1 * damage}\n{color.END}")
                        
                if(damage >= 7):
                    self.enable_sp_attack = True
                    
        return damage
                        
    def takeDamage(self, amount: int):
        if self.hitPoints >= amount:
            self.hitPoints -= amount
            # if we actually just healed, make sure
            # we don't exceed max HP
            if self.hitPoints > self.maxHitPoints:
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0

    def ai(self, sp_attack) -> int:
        if(sp_attack == True):
            roll = self.d20.roll()
            if roll <= 10:
                return "yes"
            else:
                return "no"
        else:
            attack_type = 0
            roll = self.d20.roll()
            # 13 or greater on a d20
            if roll <= 12:  # 60%
                # Fire breath used more often
                attack_type = 1
            elif roll <= 17:  # 25%
                # powerful bite used less often
                attack_type = 2
            else:
                # heal 15 %
                attack_type = 3
            return attack_type
