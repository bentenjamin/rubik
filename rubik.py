import sys
import helper
import cube
import solve
import time

def main():
    args = sys.argv
    debug = False
    i = 0
    #check for -v (debug) or too many args
    if len(args) == 3:
        while i < len(args):
            if args[i] == "-v":
                debug = True
                del args[i]
                i = 0
            i += 1
    if len(args) != 2:
        print("invalid number/type of arguments")
        return False

    #allow user to choose how long the scramble is
    if sys.argv[1] == "-r":
        number = input("How many moves would you like to scramble? ")
        while not helper.is_int(number):
            print("please provide a positive integer number for how many moves you want generated")
            number = input("How many moves would you like to scramble? ")
        demo_cube = cube.Cube()
        print("Starting Cube:", demo_cube)
        run_cube(demo_cube, demo_cube.scramble(int(number)), 1, debug)

    #default random 20 move scramble
    elif sys.argv[1] == "-d":
        demo_cube = cube.Cube()
        print("Starting Cube:", demo_cube)
        run_cube(demo_cube, demo_cube.scramble(20), 1, debug)

    #runs the scramble 100 times with given amount of moves
    elif sys.argv[1] == "-avg":
        if debug:
            print("debug method cannot be run in conjunction with pretty print!")
        number = input("How many moves would you like to scramble? ")
        while not helper.is_int(number):
            print("please provide a positive integer number for how many moves you want generated")
            number = input("How many moves would you like to scramble? ")
        average_100(number)
    
    elif sys.argv[1] == "-p":
        if debug:
            print("debug method cannot be run in conjunction with pretty print!")
        pretty_print()

    #take user input for how to scramble the cube
    else:
        instructions = sys.argv[1]
        split_instructions = instructions.split()
        for instruction in split_instructions:
            if len(instruction) not in (1, 2):
                print ("{} is not a correct instruction (length in correct), please try again".format(instruction))
                exit()
            if instruction[0] not in ('F', 'B', 'R', 'L', 'U', 'D'):
                print ("{} is not a correct instruction (first character incorrect), please try again".format(instruction))
                exit()
            if len(instruction) == 2:
                if instruction[1] not in ('2', '\''):
                    print ("{} is not a correct instruction (second character incorrect), please try again".format(instruction))
                    exit()
        demo_cube = cube.Cube()
        print("Starting Cube:", demo_cube)
        run_cube(demo_cube, split_instructions, 0, debug)

#starts the scramble and initiates the solve and optimsation process and prints the cube
def run_cube(cube, moves, scramble, debug):
    if debug:
        cube.debug = True
    if scramble:
        #comment the below line out when printing with commas
        print("Moves used to scramble cube : ", *moves)
        # uncomment these two lines to include commas in between moves in printing(for solution checking)
        # moves = ",".join(moves)
        # print("Moves used to scramble cube : ", moves)
    else:
        cube.do_moves(moves)
        #comment the below line out when printing with commas
        print("Moves used to scramble cube : ", *moves)
        # uncomment these two lines to include commas in between moves in printing(for solution checking)
        # moves = ",".join(moves)
        # print("Moves used to scramble cube : ", moves)
    print(cube)
    sln_moves = solve.solve(cube)
    print("Solved Cube:", cube)
    if len(sln_moves) == 0:
        print("Cube already solved, no moves used.")
    else:
        print("Number of moves taken: {}".format(len(sln_moves)))
        #comment the below line out when printing with commas
        print("Solution:", *sln_moves)
        # uncomment these two lines to include commas in between moves in printing(for solution checking)
        # sln_moves = ",".join(sln_moves)
        # print("Solution:", sln_moves)

#function to run a bunch of random scrambles of specified length of moves 
# 100 times and find the average amount of moves taken to solve
def average_100(number):
    moves_no = []
    sln_moves = []
    demo_cube = cube.Cube()
    for i in range(100):
        demo_cube.scramble(int(number))
        sln_moves = solve.solve(demo_cube)
        moves_no.append(len(sln_moves))
    total = sum(moves_no)
    print("average number of moves used over 100 runs is: {}".format(total/100))

# function to show rotation of cube move by move on a random 20 move shuffle
def pretty_print():
    sleep_time = 0.1
    rube_cube = cube.Cube()
    display_cube = cube.Cube()
    scramble = rube_cube.scramble(20)
    moves = solve.solve(rube_cube)

    print(display_cube)
    time.sleep(1)
    for move in scramble:
        display_cube.exe_move(move)
        string = str(display_cube)
        string += "\nScrambling...  " + move
        print(" \033[H\033[J")
        print(string)
        time.sleep(sleep_time)
    
    print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print("Scrambled! Beep Boop calculating solution...")
    print("<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    time.sleep(2)

    for move in moves:
        display_cube.exe_move(move)
        string = str(display_cube)
        string += "\nSolving...  \nExecuted move: " + move
        print(" \033[H\033[J")
        print(string)
        time.sleep(sleep_time)
    
    print("")
    print("Solved!")

main()