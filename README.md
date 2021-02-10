# rubik
python rubics cube solver


# notes
algo - Kociemba/2-Phase Algorithm
objects or matricies for storage
time limit 1 hour

# todo
graphic representation
live visual
multiple algos?
mix generator with (default and custom)
human readable output of steps

 1  2  3
[0][1][2]
 x  y  z
-1  0  1

need to install this before running
pip install string-color

python rubik.py -r
- call random moves generator and asks you how many moves you want to generate. prints the moves and then the scrambled cube

python rubik.py -d
- call random moves generator with a default number of 20 moves. prints the moves and then the scrambled cube

python rubik.py "example list of moves"
- scrambles the cube and prints the scrambled cube

python rubik.py -v "other instruction"
- only called with one of the other above arguments, cannot run on its own. will produce a step by step process of the algorithms used and the state of the cube after each algorithm in a 2D layout.
