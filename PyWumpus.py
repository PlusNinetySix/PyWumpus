import random
from rooms import RoomInfo

arrow = 3

with open("rooms.txt", "r") as ins:
    rooms = []
    array = []
    ins.readline()
    for line in ins:
        array.append(line)
        r = line.split(" ")
#         print(r)
        roomnum = r[0]
        adj = [int(x) for x in r[1:]]
        desc = ins.readline()
        rooms.append(RoomInfo(roomnum, adj.copy(), desc))
        

#Sets the variables for the rooms.
def roomvar(rooms, spider, pit):
    hazards = random.sample(rooms[1:], k=spider+pit+3)

#This function is run whenever the user chooses to move.
def move():
    global currentRoom
    try:
        m = int(input('Which room do you want to go to?\n'))
        #print(rooms[currentRoom-1].adj)
        if rooms[currentRoom-1].isAdj(m):
            currentRoom = m
            #print('You can go into rooms {0}, {1}, and {2}'.format(rooms[0]))
            print('You are in room {0}'.format(currentRoom))
            print(rooms[currentRoom-1].getDesc())
        else:
            print('Room inaccessible. Please try again.')
    except ValueError:
        print("Not a number. Please input a number.")

#This function is run whenever the user chooses to shoot.
def shoot():
    global currentRoom
    try:
        s = int(input('Into which room?\n'))
        if rooms[currentRoom-1].isAdj(s):
            currentRoom = s
            print('You have shot into room {0}'.format(currentRoom))
        global arrow
        arrow -= 1
        print('You now have {0} arrow(s) left.'.format(arrow))
        if arrow <= 0:
            print('You have run out of arrows. You will need to find a room with arrows in it.')
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