# attacks:
# Fire breath - deals less damage but hits more often
# Powerful Bite - deals the most damage but hits less often
# Heal with magical scales
# hit three times then you use a special attack - Tail Whip - large amount of damage that never misses

from die2 import Die
import color


class Dragon:
    def __init__(self, is_computer):
        self.nickname = 'Dragon'
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)
        self.numHits = 0

        # set max hit points
        # Dragon uses six d10 to calculate their starting Hit Points.
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
        self.is_computer = is_computer

# This method determines what action the dragon will perform
# depending on if it is player or computer controlled
    def attack(self):
        damage = 0
        #numHits = 0  # keep track of number of hits

        if not self.is_computer:  # if player controlled

            if self.numHits == 2:  # check number of hits
                special_attack = input("Would you like to use Tail Whip? (yes/no): ")
                if str.lower(special_attack) == "y" or str.lower(special_attack) == "yes":
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll() + self.d6.roll()  # 4d6
                    print(f"{color.GREEN}You hit with Tail Whip for {damage}\n{color.END}")
                    self.numHits = 0  # reset the number of hits

                else:  # default to regular options
                    pass
            else:  # continue to next statement
                pass

            # ask user to specify attack type
            attack_type = int(input("How would you like to attack?\n"
                                    "1. Your Breath of Fire\n"
                                    "2. Your Powerful Bite\n"
                                    "3. Use Magic Scales to Heal\n"
                                    "Enter choice: "))
            if attack_type == 1:  # Breath of fire (hits more often with less damage)
                if self.d20.roll() >= 13:  # hits on rolls of 13 or greater
                    damage = self.d6.roll() + self.d6.roll()  # rolls 2 d6 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                    self.numHits += 1  # update number of hits

                else:
                    print(f"{color.RED}You miss!\n{color.END}")

            elif attack_type == 2:  # powerful bite (hits less often with more damage)
                if self.d20.roll() >= 16:  # hits on rolls of 16 or greater
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # rolls 3 d6 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                    self.numHits += 1  # update number of hits

                else:
                    print(f"{color.RED}You miss!\n{color.END}")

            else:  # player chooses healing (attack_type == 3) OR invalid entry results in healing action
                damage = -1 * self.d6.roll()  # roll 1 d6 and add result to HP
                print(f"{color.GREEN}You heal for {-1 * damage}\n{color.END}")

        elif self.is_computer:  # computer controlled dragon uses __ai method to determine attack type
            attack_type = self.ai()  # roll attack die
            damage = 0

            # Check to see how many hits
            if self.numHits == 2:  # if computer hits twice 50% chance of using tail whip
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll() + self.d6.roll()  # 4d6
                print(f"{color.GREEN}Dragon hits with Tail Whip for {damage}\n{color.END}")
                self.numHits = 0

            if attack_type == 1:  # fire breath
                if self.d20.roll() >= 13:  # do we hit?
                    damage = self.d6.roll() + self.d6.roll()  # 2d6
                    print(f"{color.GREEN}Dragon hits with fire breath for {damage}\n{color.END}")
                    self.numHits += 1  # update number of hits
                else:
                    print(f"{color.RED}Dragon misses with fire breath!\n{color.END}")

            elif attack_type == 2:  # powerful bite
                if self.d20.roll() >= 16:
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                    print(f"{color.GREEN}Dragon hits with powerful bite for {damage}\n{color.END}")
                    self.numHits += 1  # update number of hits
                else:
                    print(f"{color.RED}Dragon misses with powerful bite!\n{color.END}")
            else:  # heal
                damage = -1 * self.d6.roll()
                print(f"{color.GREEN}Dragon uses magical scales to heal for {-1 * damage}\n{color.END}")
        else:
            pass  # is_computer should always either be T/F

        # return the damage
        #  print(damage)  debugging purposes
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

    def ai(self) -> int:
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
