from die2 import Die
import color


class Mugwump:
    def __init__(self, is_computer):
        self.d100 = Die(100)
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d6 = Die(6)

        # set max hit points
        # Mugwump uses six d10 to calculate their starting Hit Points.
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = int(self.maxHitPoints)  # start perfectly healthy
        self.is_computer = is_computer
        self.nickname = 'Mugwump'

# This method determines what action the mugwump performs
# depending on if it is player or computer controlled
    def attack(self):
        damage = None

        if not self.is_computer:  # if player controlled
            # ask user to specify attack type
            attack_type = int(input("How would you like to attack?\n"
                                    "1. Your Razor Sharp Claws\n"
                                    "2. Your Fangs of Death\n"
                                    "3. Lick your wounds and heal\n"
                                    "Enter choice: "))
            if attack_type == 1:  # Razor sharp claws
                if self.d20.roll() >= 13:  # hits on rolls of 13 or greater
                    damage = self.d6.roll() + self.d6.roll()  # rolls 2 d6 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}You miss!\n{color.END}")
            elif attack_type == 2:  # fangs of death
                if self.d20.roll() >= 16:  # hits on rolls of 16 or greater
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # rolls 3 d6 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                else:
                    print("You miss\n")
            else:  # player chooses healing attack type (attack_type == 3) OR invalid entry results in healing action
                damage = -1 * self.d6.roll()  # roll 1 d6 and add result to HP
                print(f"{color.GREEN}You heal for {-1 * damage}\n{color.END}")

        elif self.is_computer:  # computer controlled mugwump uses __ai method to determine attack type
            attack_type = self.ai()  # roll attack die
            damage = 0

            if attack_type == 1:
                if self.d20.roll() >= 13:  # do we hit?
                    damage = self.d6.roll() + self.d6.roll()  # 2d6
                    print(f"{color.GREEN}Mugwump hits with claws for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}Mugwump misses with claws\n{color.END}")

            elif attack_type == 2:
                if self.d20.roll() >= 16:
                    damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                    print(f"{color.GREEN}Mugwump hits with fangs for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}Mugwump misses with fangs\n{color.END}")
            else:
                damage = -1 * self.d6.roll()
                print(f"{color.GREEN}Mugwump heals for {-1 * damage}\n{color.END}")
        else:
            pass  # is_computer should always either be T/F

        if damage is None:
            damage = 0  # Set damage to 0 if it remains none

        # return the damage
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

    def ai(self) -> int:  # __ means private
        attack_type = 0
        roll = self.d20.roll()
        # 13 or greater on a d20
        if roll <= 12:  # 60%
            # Razor-Sharp Claws
            attack_type = 1
        elif roll <= 17:  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15 %
            attack_type = 3
        return attack_type


class Warrior:
    def __init__(self, is_computer):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d8 = Die(8)
        self.d4 = Die(4)

        # hitpoints, max is set
        # Warrior uses four d10 to calculate their starting Hit Points.
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
        self.is_computer = is_computer
        self.nickname = 'Warrior'

    def attack(self):
        # Initial damage is set to none
        damage = None

        if not self.is_computer:  # is user selects player controlled
            attack_type = int(input("How would you like to attack?\n"
                                    "1. Your Trusty Sword\n"
                                    "2. Your Shield of Light\n"
                                    "Enter choice: "))

            # roll attack die and determined results of attack
            if attack_type == 1:  # trusty sword
                if self.d20.roll() >= 12:
                    damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}You miss!\n{color.END}")
            elif attack_type == 2:  # shield of light
                if self.d20.roll() >= 6:
                    damage = self.d4.roll()  # 1d4 damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}You miss\n{color.END}")
            else:  # default to using sword if invalid entry
                print("You use your trusty sword!\n")
                if self.d20.roll() >= 12:
                    damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                    print(f"{color.GREEN}You hit for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}You miss!\n{color.END}")

        elif self.is_computer:  # if user selects computer controlled
            attack_type = self.ai()
            # roll attack die and determined results of attack
            if attack_type == 1:  # trusty sword
                if self.d20.roll() >= 12:
                    damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                    print(f"{color.GREEN}The Warrior hits with his trusty sword for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}The Warrior misses with his sword!\n{color.END}")
            else:  # (attack_type == 2): # shield of light
                if self.d20.roll() >= 6:  # do we hit
                    damage = self.d4.roll()  # 1d4 damage
                    print(f"{color.GREEN}The Warrior hits with his shield of light for {damage}\n{color.END}")
                else:
                    print(f"{color.RED}The Warrior misses with his shield of light!\n{color.END}")
        else:
            pass  # is_computer should always be T/F

        if damage is None:
            damage = 0

        # return the damage
        return damage

    def ai(self) -> int:  # __ means private
        attack_type = 0

        roll = self.d20.roll()
        if roll <= 12:  # 60% chance
            # Trusty Sword
            attack_type = 1
        else:
            # Shield of Light
            attack_type = 2
        return attack_type

    def takeDamage(self, amount: int):
        if self.hitPoints >= amount:
            self.hitPoints -= amount
        else:
            self.hitPoints = 0
