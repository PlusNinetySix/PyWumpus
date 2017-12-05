import random
import rooms


with open("rooms.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
        room0 = line.split(", ", 1)
        #print(room0)


def roomvar():
    for i in range(2):
        pass

def move():
    pass

def shoot(arrow):
    arrow -= 1 #do global
    print('You now have ' + str(arrow) + ' arrow(s) left.')

def main():
    arrow = 3
    currentRoom = 1
    print('Welcome to Hunt the Wumpus!\nYou are in room 1.\nYou have three arrows left.')
    while True:
        mors = input('What will you do? m for moving, s for shooting\nType exit to quit.\n')
        if mors == 'm':
            move()
        elif mors == 's':
            shoot(arrow)
        elif mors == 'exit':
            print('Goodbye!')
            break
        else:
            print('Invalid syntax. Please Try again.')

main()