import random       # Pythons built in system for generating random numbers (all languages have rng generators)


class Hero:
    def __init__(self, name, health, power):                                # Hero gets properties name, health, and power
        self.name = name                                        
        self.health = health
        self.power = power

    def attack(self, boss):                                                 # attack() gets one param boss (self won't be required when passing arguments)
        if self.health > 0:                                                 # check if health is greater than 0
            damage = random.randint(1, 3) * self.power                      # set damage to random integer between 1
            print(f"{self.name} strike {boss.name} for {damage} damage!")   # print the result
            boss.health -= damage                                           # Use operator -= to subtract damage from boss's health


