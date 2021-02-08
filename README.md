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

python rubik.py "example list of moves"
- scrambles the cube and prints the scrambled cube

take in face and move and execute move as if in relation to face, not incl top/bot. start white face up

R from front face equals back face.
