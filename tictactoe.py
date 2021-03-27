#I'msa fegort y zit atumpt swill prods flale
import string
import random
spot = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
csmarter = 0
counter = 0
mode = 0
difficulty = ""
done = False
into_rounds = False
def board():
    print(spot[0], spot[1], spot[2])
    print(spot[3], spot[4], spot[5])
    print(spot[6], spot[7], spot[8])
def who_turn():
    #states turn
    global counter, first
    if (first == 0 and mode == 1) or (counter == 1 and first == 4 and mode == 1):
        print("Your({}) turn.".format(psymbol))
        play(psymbol)
        first = 4
    elif (first == 0 and mode == 2) or (counter == 1 and first == 5 and mode == 2):
        print("Player 1's({}) turn.".format(psymbol))
        play(psymbol)
        first = 5
    elif (first == 1 and mode == 1) or (counter == 3 and first == 4 and mode == 1):
        counter = 3
        print("Computer's({}) turn.".format(csymbol))
        cplay()
        first = 4
    elif (first == 1 and mode == 2) or (counter == 2 and first == 5 and mode == 2):
        print("Player 2's({}) turn.".format(p2symbol))
        play(p2symbol)
        first = 5
def cplay(): #this one may be confusing :^)
    global csmarter, CONDITIONS, counter, dificulty, engineer_bap, spot
    played = False
    the_move = [0,1,2]
    i = 0
    if difficulty == "2":
        while not played:
            for i in range(0, 8):
                please = CONDITIONS[i]
                #if a=b a=c b=c a!=b!=c
                if (spot[please[0]] == spot[please[1]] != spot[please[2]]) or (spot[please[0]] != spot[please[1]] == spot[please[2]]) or (spot[please[0]] == spot[please[2]] != spot[please[1]]) and (spot[please[0]] != spot[please[1]] != spot[please[2]]) :
                    the_move = please
                i += 1
            if spot[the_move[0]] == spot[the_move[1]] and spot[the_move[2]] == engineer_bap[the_move[2]]:
                cmove = the_move[2]
                spot[cmove] = csymbol
                counter = 1
                played = True
            elif spot[the_move[0]] == spot[the_move[2]] and spot[the_move[1]] == engineer_bap[the_move[1]]:
                cmove = the_move[1]
                spot[cmove] = csymbol
                counter = 1
                played = True
            elif spot[the_move[1]] == spot[the_move[2]] and spot[the_move[0]] == engineer_bap[the_move[0]]:
                cmove = the_move[0]
                spot[cmove] = csymbol
                counter = 1
                played = True
            elif not played and counter == 3:
                cmove = random.randint(0, 8)
                while not played:
                    if spot[cmove] != str(cmove + 1):
                        cmove = random.randint(0, 8)
                    else:
                        counter = 1
                        spot[cmove] = csymbol
                        played = True
    elif difficulty == "1":
        cmove = random.randint(0, 8)
        played = False
        while not played:
            if spot[cmove] != str(cmove + 1):
                cmove = random.randint(0, 8)
            else:
                counter = 1
                spot[cmove] = csymbol
                played = True
CONDITIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def win_check():
    global CONDITIONS
    for [a, b, c] in CONDITIONS:
        if spot[a] == spot[b] == spot[c]:
            if mode == 1:
                if spot[b] == psymbol:
                    board()
                    print("Congratz, You({}) Won!".format(psymbol))
                    restart()
                else:
                    board()
                    print("The Computer({}) Won, You Lose.".format(csymbol))
                    restart()
            elif mode == 2:
                if spot[b] == psymbol:
                    board()
                    print("Player One({}) Won!".format(psymbol))
                    restart()
                else:
                    board()
                    print("Player Two({}) Won!".format(p2symbol))
                    restart()
def restart():
    global counter, csmarter, into_rounds, mode, spot
    counter = 0
    csmarter = 0
    into_rounds = False
    spot = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    again = (input("Restart(Y)    Menu(Any other letters except 'Y'): ")).upper()
    if again != "Y":
        print()
        mode = 0
def play(symbol):
    global counter
    symbol_copy = symbol
    move = input("Pick a spot (1-9): ")
    played = False
    while not played:
        if len((move)) != 1 or spot[int(move)-1] != (move):
            print("Sorry, that spot has been taken or is not on the board. Pick another.")
            move = input("Pick a spot (1-9): ")
        else: played = True
    if mode == 1:
        spot[int(move)-1] = symbol
        counter = 3
    elif mode == 2:
        spot[int(move)-1] = symbol
        if symbol_copy == p2symbol:
            counter = 1
        elif symbol_copy == psymbol:
            counter = 2
engineer_bap = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def move_check():
    #   ;)   checks whole board for available moves
    global engineer_bap
    sentry_gun = 0
    for k in range(9):
        if spot[k] != engineer_bap[k]:
            sentry_gun += 1
        k += 1
    if sentry_gun == 9:
        print("Draw!")
        restart()
while not done:
    #menu
    while mode == 0:
        #Game mode selection
        print("<Please select a gamemode>")
        mode = int(input("Single Player(1) or Two Player(2): "))
        while mode != 1 and mode != 2:
            print("Please enter a valid number")
            mode = int(input("Single Player(1) or Two Player(2): "))
    #Single player
    while mode == 1:
        first = random.randint(0, 1)
        difficulty = input("Select Computer difficulty - Easiest(1) Easy(2): ").upper()
        while (difficulty != "1" and difficulty != "2") or len(difficulty) != 1:
            print("Please select a difficulty(1 or 2).")
            difficulty = input("Select Computer difficulty - Easiest(1) Easy(2): ").upper()
        #picking symbol
        psymbol = (input("Pick your symbol (letter): ")).upper()
        while (psymbol).isdigit() or len(psymbol) != 1:
            print("Please select a letter.")
            psymbol = (input("Pick your symbol (letter): ")).upper()
        csymbol = random.choice(string.ascii_uppercase)
        while csymbol == psymbol:
            csymbol = random.choice(string.ascii_uppercase)
        into_rounds = True
        while into_rounds:
            board()
            move_check()
            who_turn()
            print()
            win_check()
    #Two Player
    while mode == 2:
        first = random.randint(0, 1)
        #picking symbol
        psymbol = (input("Pick your symbol Player One(letter): ")).upper()
        while (psymbol).isdigit() or len(psymbol) != 1:
            print("Please select a letter.")
            psymbol = (input("Pick your symbol Player One(letter): ")).upper()
        p2symbol = (input("Pick your symbol Player Two(letter): ")).upper()
        while (p2symbol).isdigit() or p2symbol == psymbol or len(p2symbol) != 1:
            print("Please select a letter.")
            p2symbol = (input("Pick your symbol Player Two(letter): ")).upper()
        into_rounds = True
        while into_rounds:
            board()
            move_check()
            who_turn()
            print()
            win_check()