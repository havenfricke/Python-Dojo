from Hero import Hero               # import the Hero class
from Boss import Boss               # import the Boss class
import gameState                    # import the game state

heroHealth = 100                    # Set Hero stats                     
heroPower = 5

bossHealth = 500                    # Set boss stats
bossPower = 10

for index in range(3):                                              # This is a for loop with a set number of iterations at 3 using range(3)
    name = input(F"Enter name for Hero {index + 1}: ")              # Ask user for input of hero name
    heroToAdd = Hero(name, heroHealth, heroPower)                   # set heroToAdd to an instantiated Hero()
    gameState.currentParty.append(heroToAdd)                        # reference the game state's current party and append() heroToAdd (add to end of array)

bossName = input(f"\n Input boss name: ")                           # Ask user to set the Boss's name
bossToAdd = Boss(bossName, bossHealth, bossPower)                   # set bossToAdd to an instantiated Boss()
gameState.bossTarget = bossToAdd                                    # reference the game state's bossTarget and set as bossToAdd

while gameState.bossTarget.health > 0 and any(hero.health > 0 for hero in gameState.currentParty): # While loop that runs while bossTarget's health property is great than 0
                                                                                                   # and use any() (a built-in python "searcher method") to check condition (hero.health > 0)
    print(f"\n--- Round {gameState.currentRound} ---")                                             # for current party array in game state. This will evaluate to True or False.     

    for hero in gameState.currentParty:                                                            # Loop through hero array in game state's current party array
        if hero.health > 0 and gameState.bossTarget.health > 0:                                    # check if th current hero in the for loop's health is > 0 and if game state's boss target             
            input(f"Press Enter for {hero.name} to attack...")                                     # health is above 0. These evaluate to true or false
            hero.attack(gameState.bossTarget)                                                      # Ask user to press enter then call her to perform an attack on the game state's boss target  

    if gameState.bossTarget.health > 0:                                                            # check if boss targets health is above 0 
        input(f"Press Enter to see what {gameState.bossTarget.name} does...")                      # Ask for user to press enter for the boss to attack  
        gameState.bossTarget.attack(gameState.currentParty)                                        # After the user presses enter, call to game state's boss target and call attack method     

    print("\n--- BOSS STATUS ---")                                                                 # once all players and boss have attacked, print boss status and party status to  
    print(f"{gameState.bossTarget.name} has {gameState.bossTarget.health} health remaining!")      # check the game progress / state 

    print("\n--- PARTY STATUS ---")
    for hero in gameState.currentParty:                                                            # Loop through the heros is game state's current party
        if hero.health > 0 and gameState.bossTarget.health > 0:                                    # check if the hero at teh for loop's current index position is great than 0 
            print(f"Hero: {hero.name}, Remaining Health: {hero.health}")                           # and if the game state's boss target's health is greater than 0 

    gameState.currentRound += 1                                                                    # increment game state's current round by 1  

print("\n The battle is over...")                                                                  # If the while loop's conditions evaluate to false, jump out of the loop, print this line, 
                                                                                                   # then exit the program. 