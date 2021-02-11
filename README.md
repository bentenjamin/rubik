# rubik
python rubiks cube solver
Rubik is a rubik's cube solver programme written in python. It takes in a list of instructions to scramble a cube, and then solves the cube and returns the list of moves used in the solution. The cube object stores the cube in a 3x3x3 array of cubies, containing colours and an xyz location.

The algorithm used to solve the cube is the human method:
white cross
white corners
middle layer
bottom layer cross
bottom layer corners.

in order to run this project you need to:
install a colour library: pip install string-color numpy
clone the repository and cd into the folder. 

to run the project:
python3 rubik.py "arguments - see examples below

python3 rubik.py -r
- call random moves generator and asks you how many moves you want to generate. prints the moves and then the scrambled cube, and then solves it

python rubik.py -d
- call random moves generator with a default number of 20 moves. prints the moves and then the scrambled cube and solves it

python rubik.py "example list of moves"
- scrambles the cube and prints the scrambled cube, and then solves it.

python rubik.py -v "other instruction"
- only called with one of the other above arguments, cannot run on its own. will produce a step by step process of the algorithms used and the state of the cube after each algorithm in a 2D layout.

python rubik.py -avg
- run 100 solves and give the average amount of moves

python rubik.py -p
- Pretty print. prints the cube and the move it executes as it solves
