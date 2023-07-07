"""
    Course: CS5980
    Summer 2023
    Battle Simulator 3000
    Name: FIXME
    Created: FIXME
"""
from die import Die
class Warrior:



    def __init__(self, aiController:bool):  # for homework 4 #, aiController:bool):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.d8 = Die(8)
        self.d4 = Die(4)

        # hitpoints, max is set
        # Warrior uses four d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy
        
        self.aiController = aiController

    # add methods here

    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Mugwump heals itself
     """

    def attack(self, attack_type:int) -> int:
        # unlike mugwump, warrior's attack type is passed
        # in as a parameter.
        if(self.aiController):
            attack_type = self.__ai()

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1): # trusty sword
            if (self.d20.roll() >= 12):  # do we hit?
                damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                print(f"Warrior hit for {damage}")
            else:
                print("Warrior miss!")
        else:  # (attack_type == 2): # shield of light
            if (self.d20.roll() >= 6): # do we hit
                damage = self.d4.roll()  # 1d4 damage
                print(f"Warrior hit for {damage}")
            else:
                print("Warrior miss")


        # return the damage
        return damage

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    def takeDamage(self, amount: int):
        if ((self.hitPoints >= amount)):
            self.hitPoints -= amount
        else:
            self.hitPoints = 0
            
    def __ai(self) -> int:  # __ means private # testable on range of output
        attack_type = 0
        roll = self.d20.roll()
        # 13 or greater on a d20
        if (roll <= 12):  # 60%
            # Razor-Sharp Claws
            attack_type = 1
        elif (roll <= 17):  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15 %
            attack_type = 3

        return attack_type