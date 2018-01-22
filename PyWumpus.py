import random
#import rooms

arrow = 3

with open("rooms.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
        r = line.split(" ")
        #print(r[0])

#Sets the variables for the rooms.
def roomvar():
    wroom = random.randint(0,14)
    proom1 = random.randint(0,14)
    proom2 = random.randint(0,14)
    sroom1 = random.randint(0,14)
    sroom2 = random.randint(0,14)

#This function is run whenever the user chooses to move.
def move():
    try:
        m = int(input('Which room do you want to go to?\n'))
        print("t")
    except ValueError:
        print("Not a number. Please input a number.")

#This function is run whenever the user chooses to shoot.
def shoot():
    try:
        s = int(input('Into which room?\n'))
        global arrow
        arrow -= 1
        print('You now have ' + str(arrow) + ' arrow(s) left.')
        if arrow <= 0:
            print('You have run out of arrows. Game over!')
            quit()
    except ValueError:
        print("Not a number. Please input a number.")

#The function that allows the game to run.
def main():
    global currentRoom
    currentRoom = 1
    print('Welcome to Hunt the Wumpus!\nYou are in room 1.\nYou have three arrows left.')
    while True:
        mors = input('What will you do? m for moving, s for shooting\nType exit to quit.\n')
        if mors == 'm' or mors == 'M':
            move()
        elif mors == 's' or mors == 'S':
            shoot()
        elif mors == 'exit':
            print('Goodbye!')
            break
        else:
            print('Invalid syntax. Please Try again.')

main()