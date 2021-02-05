import sys
import helper
import cube

def main():
    if len(sys.argv) != 2:
        print("invalid number of arguments")
        return False
    elif sys.argv[1] == "-r":
        number = input("How many moves would you like to scramble? ")
        while not helper.is_int(number):
            print("please provide a positive integer number for how many moves you want generated")
            number = input("How many moves would you like to scramble? ")
        moves = helper.moves_generator(int(number))
        print(*moves)
        demo_cube = cube.Cube()
        demo_cube.execute_moves(moves)
        demo_cube.print_cube()
        #then solve
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
        print("after the error checking this should scramble and solve now")
        demo_cube = cube.Cube()
        # demo_cube.execute_moves(["F", "B", "L2"])
        demo_cube.execute_moves(split_instructions)
        demo_cube.print_cube()
        # demo_cube.execute_moves(["L2", "B'", "F'"])
        # demo_cube.print_cube()
        #solve