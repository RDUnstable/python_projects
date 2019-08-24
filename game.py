# THIS IS A LITTLE FUNNY GAME WHERE YOU AND YOUR SYSTEM COMPETE TO REACH A TARGET NUMBER(50 IN THIS CASE).IT USES THE RANDOM MODULE OF PYTHON
# AND RETURNS RANDOM NUMBERS THOSE ADD UP TO REACH THE GOAL :P.......YOU HAVE TO JUST PRESS THE SPECIFIED BUTTON TO MAKE YOUR TURN.
#.......................................LETS'S TRY IT AND SEE WHO WINS :P.......................................................
#THIS CODE IS FULLY FUNCTION BASED..............................................................................................
import random
import sys

probable = [2,2,2,2,2,10]

me = 0
comp = 0

flagme = 0
flagcomp = 0

flaggame = 0

print("Here the game starts. Reach 50 to win the game................")

l = [1,2,3,4,5,6]

def main_game():
    global me
    global comp
    global probable

    print("Your main turn.......hit y: ")
    c = input()
    if c == 'y':
        p = random.choices(l,weights = probable)
        me += p[0]

    h = random.choices(l,weights = probable)
    comp += h[0]

    if me >= 50 or comp >= 50:
        if me >= 50:
            print("You won!!!!!!")
            sys.exit()

        elif comp >= 50:
            print("Computer won..............")
            sys.exit()
    print("Updated score: you : ",me,"comp : ",comp)


def me_first():
    global me
    global comp
    global probable

    print("Your turn.......hit y: ")
    a = input()
    if a == 'y':
        b = random.choices(l,weights = probable)
        me += b[0]

        if(me >= 50):
            print("You won")
            sys.exit()

    k = random.choices(l,weights = probable)
    if k == 6:
        loop()

    else:
        print("You : ",me,"comp : ",comp)
        me_first()


def comp_first():
    global me
    global comp
    global probable

    print("You haven't started yet......hit y: ")
    f = input()
    
    g = random.choices(l,weights = probable)
    comp += g[0]
    if comp >= 50:
        print("Computer won.....")
        sys.exit()

    if f == 'y':
        r = random.choices(l,weights = probable)
        if r == 6:
            loop()

        else:
            print("You : ",me,"comp : ",comp)
            comp_first()

def loop():
    global me
    global comp
    global probable

    while(me < 50 or comp < 50):
        main_game()

def start():
    global probable
    
    print("Let's start the game.............")
    print("Enter s to start: ")
    i = input()
    if i == 's':

        v = random.choices(l,weights = probable)
    com = random.choices(l,weights = probable)

    if v[0] == 6 and com[0] < 6:

        me_first()

    elif v[0] < 6 and com[0] == 6:
        comp_first()

    elif v[0] == 6 and com[0] == 6:
        loop()

    elif v[0] < 6 and com[0] < 6:
        start()


start()

if me >= 50:
    print("You won!!!!!!!!")

elif comp >= 50:
    print("Computer won..........")
        
