import sys
import helper
import cube
import solve

def main():
    args = sys.argv
    debug = False
    i = 0
    if len(args) == 3:
        while i < len(args):
            if args[i] == "-v":
                debug = True
                del args[i]
                break
            i += 1
        else:
            print("invalid number/type of arguments")
            return False
    if len(args) != 2:
        print("invalid number/type of arguments")
        return False

    #allow user to choose how  long the scramble is
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
        print("Moves used to scramble cube : ", *moves)
    else:
        cube.do_moves(moves)
        print("Moves used to scramble cube : ", *moves)
    print(cube)
    solve.solve(cube)

main()