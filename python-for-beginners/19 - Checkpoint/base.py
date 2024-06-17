# this file is the main file for the program
#-----------------------------------------


# import the required modules
# -----------------------------------------
import random
import time

# create constant variables for the program
#  -----------------------------------------
GameOver = False
PlayerLevel = 0
PlayerHealth = PlayerLevel + 100
PlayerStrength = PlayerLevel + 10

map =   [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

PlayX = 6
PlayY = 7
map[PlayX][PlayY] = 1

exitX = random.randint(0,14)
exitY = random.randint(0,12)
map[exitX][exitY] = 5

# create the def() functions for the program
# -----------------------------------------
def BoardUpdate():
    for row in map:
        print(row)

def Movement():
    global PlayX, PlayY
    direction = input('Which way will you move? (N - S - E - W) ')
    direction = direction.lower()
    if direction == 'n':
        if PlayX > 0:
            map[PlayX][PlayY] = 7
            PlayX -= 1
            map[PlayX][PlayY] = 1
        else:
            print("You walk directly into a wall and take 1d6 bludgeoning damage. Don't be a dummy!")
            PlayerHealth - random.randint(1,6)
    elif direction == 's':
        if PlayX < 4:
            map[PlayX][PlayY] = 7
            PlayX += 1
            map[PlayX][PlayY] = 1
        else:
            print('You walk into a wall and crush your nose on it. Ouch.')
            PlayerHealth - random.randint(1,6)
    elif direction == 'e':
        if PlayY < 4:
            map[PlayX][PlayY] = 7
            PlayY += 1
            map[PlayX][PlayY] = 1
        else:
            print("You walk into a wall in front of one of your friends. They use vicious mockery on you and you take 1d6 damage.")
            PlayerHealth - random.randint(1,6)
    elif direction == 'w':
        if PlayY > 0:
            map[PlayX][PlayY] = 7
            PlayY -= 1
            map[PlayX][PlayY] = 1
        else:
            print('You cannot move in that direction')
    else:
        print('I do not understand that direction')


# create the main loop for the program
# -----------------------------------------
while GameOver == False:
    BoardUpdate()
