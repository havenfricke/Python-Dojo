import random   # Pythons built in system for generating random numbers (all languages have rng generators)

class Boss:
    def __init__(self, name, health, power):                # Class Boss gets properties name, health, and power
        self.name = name
        self.health = health
        self.power = power

    def attack(self, party):                                # attack gets one params party (self won't be required when passing arguments)
        livingHeros = []                                    # instantiate and empty array
        for hero in party:
            if hero.health > 0:
                livingHeros.append(hero)                    # array.append() is a built in method to add a variable to the end of an array
    
        if livingHeros:                                     # Truthy statement
            target = random.choice(livingHeros)             # .choice(array) checks length of array and chooses a random index from the array passed to it
            print(f"\n{self.name} lunges at {target.name}")
            damage = random.randint(1, 3) * self.power      # Choose a random integer between 1 and 10
            target.health -= damage                         # Perform -= operator to subtract from target's health
            print(f"\n{target.name} takes {damage} damage! (HP: {target.health})") # string interpolate the results


