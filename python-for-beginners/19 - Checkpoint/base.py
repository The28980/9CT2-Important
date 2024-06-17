# this file is the main file for the program
#-----------------------------------------
import random
import time

GameOver = False # create a variable to control the game loop
PlayerHealth = 100 # create a variable to store the player's health
PlayerHealthMAX = 100
PushYourLuck = 0
DivineJudgmentDeathBlowDamage = 0

#----------------------------------------- SET UP THE GAME BOARD -----------------------------------------
#create a 5x5 game board. 0 = empty, 1 = player, 2 = enemy, 3 = treasure, 4 = trap, 5 = exit, 6 = boss, 7=visited
map = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]

# place the player in the middle of the game board
PlayerX = 2
PlayerY = 2
map[PlayerX][PlayerY] = 1

# place the exit in a random location
exitX = random.randint(0,4)
exitY = random.randint(0,4)
map[exitX][exitY] = 5

# ----------------------------------------- SET UP THE FUNCTIONS -----------------------------------------
# create the def() functions for the program here
def printBoard():
    for row in map:
        print(row)

def movePlayer():
    global PlayerX, PlayerY, PlayerHealth
    direction = input(
        '''Which way will you move? (N - S - E - W) 
-> ''')
    direction = direction.lower()
    if direction == 'n':
        if PlayerX > 0:
            map[PlayerX][PlayerY] = 7
            PlayerX -= 1
            map[PlayerX][PlayerY] = 1
        else:
            print('The wall is right there, are you blind? (This insult makes you take 1d6 <Vicious Mockery> Psychic damage)')
            PlayerHealth = PlayerHealth - random.randint(1,6)
            print(f'Your health is now {PlayerHealth}/{PlayerHealthMAX}')
    elif direction == 's':
        if PlayerX < 4:
            map[PlayerX][PlayerY] = 7
            PlayerX += 1
            map[PlayerX][PlayerY] = 1
        else:
            print('You hit the back of your head on the wall, leaving you dazed. You take 1d6 <Dungeon Wall> Bludgeoning damage')
            PlayerHealth = PlayerHealth - random.randint(1,6)
            print(f'Your health is now {PlayerHealth}/{PlayerHealthMAX}')
    elif direction == 'e':
        if PlayerY < 4:
            map[PlayerX][PlayerY] = 7
            PlayerY += 1
            map[PlayerX][PlayerY] = 1
        else:
            print("You attempt to lean on the wall, but it's unexpectedly slippery and you fall over. You take 1d6 <Embarrassment> Psychic damage")
            PlayerHealth = PlayerHealth - random.randint(1,6)
            print(f'Your health is now {PlayerHealth}/{PlayerHealthMAX}')
    elif direction == 'w':
        if PlayerY > 0:
            map[PlayerX][PlayerY] = 7
            PlayerY -= 1
            map[PlayerX][PlayerY] = 1
        else:
            print('A fist forms in the wall and punches you. You feel like you hear a voice yelling "Back off, stranger!" You take 1d6 <Sentient Wall> Bludgeoning damage')
            PlayerHealth = PlayerHealth - random.randint(1,6)
            print(f'Your health is now {PlayerHealth}/{PlayerHealthMAX}')
    else:
        if PushYourLuck == 0:
            print("Sorry, that's not a real input!")
            PushYourLuck == PushYourLuck + 1
        elif PushYourLuck == 1:
            print("Hey player, that's not a valid input!")
            PushYourLuck == PushYourLuck + 1
        elif PushYourLuck == 2:
            print("Are you doing this on purpose?")
            PushYourLuck == PushYourLuck + 1
        elif PushYourLuck == 3:
            print("Push Your Luck one more time.")
            PushYourLuck == PushYourLuck + 1
        elif PushYourLuck == 4:
            print("*You feel a sudden chill in the air*")
            PushYourLuck == PushYourLuck + 1
        elif PushYourLuck == 5:
            print("You've been too silly player, TAKE THIS!")
            time.sleep(0.5)
            print("*Divine Judgment Death Blow*")
            DivineJudgmentDeathBlowDamage = random.randint(50,100)
            PlayerHealth = PlayerHealth - DivineJudgmentDeathBlowDamage
            print(f"Your silly self takes {DivineJudgmentDeathBlowDamage} damage!!!")
            PushYourLuck == 0
        else:
            print("Schmorugs McDorgus Ultra Mega Divine Death Beam of Utter Dematerialisation :3")
            PlayerHealth = PlayerHealth - 99999999999999999
            print("get dunked on kid (This should not be able to happen ever, if it does my code is broken)")
   
    

#check if the player has reached the exit
def checkExit():
    global GameOver
    if PlayerX == exitX and PlayerY == exitY:
        print('You step on a suspicious looking tile...')
        gameOver = True

# ----------------------------------------- MAIN LOOP -----------------------------------------
# create the main loop for the program here
while GameOver == False:
    printBoard()
    movePlayer()
    checkExit()
    time.sleep(1)
print("...You drop below the floor! But honestly, this is probably the better outcome. GG?")