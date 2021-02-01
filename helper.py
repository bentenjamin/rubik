import random

# NB, in order to simplify the best way possible, moves prior to the optimising functions should not have any 2's in them i.e the optimising function should be the only one adding "face2" moves

def moves_generator(number):
    moves_list = []
    i = 0
    moves = ["L", "U", "F", "D", "R", "B", "L'", "U'", "F'", "D'", "R'", "B'","L2", "U2", "F2", "D2", "R2", "B2"]
    while i < number:
        moves_list.append(random.choice(moves))
        i += 1
    return (moves_list)

def invert_move(move):
    if move[-1:] == "'":
        move = move[:1]
    else:
        move = move + "'"
    return move

#this needs to be the first optimisation done
def optimise_do_undo(moves):
    i = 0
    changed = False
    while i < len(moves) - 1:
        if moves[i] == invert_move(moves[i + 1]):
            del moves[i:i + 2] 
            changed = True
        else:
            i += 1
    if changed:
        optimise_do_undo(moves)
    return(moves)

#this needs to be the last optimisation done
def optimise_half_turn_metric(moves):
    i = 0
    changed = False
    while i < len(moves) - 1:
        if moves[i] == moves[i + 1]:
            # if moves[i][-1] == "2":
            #     del moves[i:i + 2]
            moves[i] = moves[i][0] + "2"
            del moves[i + 1:i + 2] 
            changed = True
        else:
            i += 1
    if changed:
        optimise_half_turn_metric(moves)
    return(moves)

#this needs to be the middle optimisation done
def optimise_3_to_1(moves):
    i = 0
    changed = False
    while i < len(moves) - 2:
        if moves[i] == moves[i + 1] == moves[i + 2]:
            moves[i] = invert_move(moves[i])
            del moves[i + 1:i + 3] 
            changed = True
        else:
            i += 1
    if changed:
        optimise_3_to_1(moves)
    return(moves)

# number = 10
# moves = ["L", "L'", 'F', "F", 'F', "B'", 'B2', 'D', "D", "L'"]
# print(moves)
# print(optimise_do_undo(moves))
# print(optimise_3_to_1(moves))
# print(optimise_half_turn_metric(moves))