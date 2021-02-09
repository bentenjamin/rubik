import sys
import helper
import cube
import solve

def main():
    if len(sys.argv) != 2:
        print("invalid number of arguments")
        return False
    elif sys.argv[1] == "-r":
        number = input("How many moves would you like to scramble? ")
        while not helper.is_int(number):
            print("please provide a positive integer number for how many moves you want generated")
            number = input("How many moves would you like to scramble? ")
        demo_cube = cube.Cube()
        moves = demo_cube.scramble(int(number))
        print(*moves)
        print(demo_cube)
        #then solve
        algos = solve.Algos(demo_cube)
        # print(algos.moves)
    elif sys.argv[1] == "-d":
        demo_cube = cube.Cube()
        moves = demo_cube.scramble(20)
        print(*moves)
        print(demo_cube)
        algos = solve.Algos(demo_cube)
        # print(algos.moves)
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
        print(demo_cube)
        # demo_cube.do_moves("F B L2")
        demo_cube.do_moves(instructions)
        print(demo_cube)
        # demo_cube.do_moves("L2 B' F'")
        # print(demo_cube)
        #solve
main()