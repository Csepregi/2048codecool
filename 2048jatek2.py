import random
import os

def points():
    print("score:",score)



def tab_start():
    global tab
    tab = []
    for i in range(4):
        tab.append([0,0,0,0])
    rand = []
    for r in range(4):
        rand.append(random.randrange(0,4))
    tab[rand[0]][rand[1]] = 2
    tab[rand[2]][rand[3]] = 2
    print("_"*32)
    print()
    for i in range(4):
        print("| %4d  | %4d  | %4d  | %4d  |" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
        print("_"*32)
        print()
    return tab
        
def random_game():
    random_index_list = []
    for x in range(4):
        for y in range(4):
            if tab[x][y] == 0:
                random_index_list.append([x,y])
    random_index = random.choice(random_index_list)
    tab[random_index[0]][random_index[1]] = 2

def move_horizontal(a,b):
    global counter
    counter = 0
    for x in range(4):
        for rep in range(3):
            for y in range(3):
                if tab[x][y+a] == 0 and tab[x][y+b] != 0:
                    tab[x][y+a] = tab[x][y+b]
                    tab[x][y+b] = 0
                    counter += 1


def move_horizontal_after_addition(a,b):
    for x in range(4):
            for y in range(3):
                if tab[x][y+a] == 0 and tab[x][y+b] != 0:
                    tab[x][y+a] = tab[x][y+b]
                    tab[x][y+b] = 0


def move_vertical(up,down):
    global counter
    counter = 0
    for y in range(4):
        for rep in range(3):
            for x in range(3):
                if tab[x+up][y] == 0 and tab[x+down][y] != 0:
                    tab[x+up][y] = tab[x+down][y]
                    tab[x+down][y] = 0
                    counter += 1

def move_vertical_after_addition(up,down):
    for y in range(4):
            for x in range(3):
                if tab[x+up][y] == 0 and tab[x+down][y] != 0:
                    tab[x+up][y] = tab[x+down][y]
                    tab[x+down][y] = 0


def add_left():
    global score
    for x in range(4):
        for y in range(3):
            if tab[x][y] == tab[x][y+1]:
                tab[x][y+1] *= 2 
                score += tab[x][y+1]
                tab[x][y] = 0
         
           

def add_right():
    global score
    for x in range(4):
        
            for y in reversed(range(3)):
                if tab[x][y] == tab[x][y+1]:
                    tab[x][y+1] *= 2
                    score += tab[x][y+1]
                    tab[x][y] = 0

def add_up():
    global score

    for y in range(4):
        
            for x in range(3):
                if tab[x+1][y] == tab[x][y]:
                    tab[x][y] *= 2
                    score += tab[x][y+1]
                    tab[x+1][y] = 0

def add_down():
    global score
    for y in range(4):
        
            for x in reversed(range(3)):
                if tab[x+1][y] == tab[x][y]:
                    tab[x][y] *= 2
                    score += tab[x][y+1]
                    tab[x+1][y] = 0

score = 0
tab_start()
while True:
    move = input("Please enter direction!:  ")
    os.system('cls' if os.name == 'nt' else 'clear')

    if move == "a":
        move_horizontal(0,1)
        add_left()
        move_horizontal_after_addition(0,1)
        if counter != 0:
            random_game()
    
    elif move == "d":
        move_horizontal(1,0)
        add_right()
        move_horizontal_after_addition(1,0)
        if counter != 0:
            random_game()

    elif move == "w":
        move_vertical(0,1)
        add_up()
        move_vertical_after_addition(0,1)
        if counter != 0:
            random_game()

    elif move == "s":
        move_vertical(1,0)
        add_down()
        move_vertical_after_addition(1,0)
        if counter != 0:
            random_game()
    
    elif move == "x":
        exit()
   

    points()
    print()
    print()
    print()
    for i in range(4):
        print("  %4d    %4d    %4d    %4d   " % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
        print()
        print()