import random
#check if a string is a number
def is_int(s):
    try: 
        int(s)
        if int(s) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

#see if all colours on a face are the same
def check_face(colours):
    i = 0
    while i < 9:
        if colours[i] != colours[0]:
            return False
        else:
            i += 1
    return True
# NB, in order to simplify the best way possible, moves prior to the optimising functions should not have any 2's in them i.e the optimising function should be the only one adding "face2" moves

#makes a move into a move in the opposite direction
def invert_move(move):
    if move[-1:] == "'":
        move = move[:1]
    elif move[-1:] == "2":
        return move
    else:
        move = move + "'"
    return move

#this needs to be the first optimisation done
#removes redundency in inverted moves
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
#shortens moves by using the "2" for two identical moves
def optimise_half_turn_metric(moves):
    i = 0
    changed = False
    while i < len(moves) - 1:
        if moves[i] == moves[i + 1]:
            moves[i] = moves[i][0] + "2"
            del moves[i + 1:i + 2] 
            changed = True
        else:
            i += 1
    if changed:
        optimise_half_turn_metric(moves)
    return(moves)

#this needs to be the middle optimisation done
#removes redundency by making 3 smae moves into 1 inverted move
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

#removes redundency by removing 4 identical moves
def optimise_4_to_1(moves):
    i = 0
    changed = False
    while i < len(moves) - 3:
        if moves[i] == moves[i + 1] == moves[i + 2] == moves[i + 3]:
            del moves[i:i + 4] 
            changed = True
        else:
            i += 1
    if changed:
        optimise_4_to_1(moves)
    return(moves)

#runs all the optimising functions to shorten moves list
def optimise_all(moves):
    optimise_do_undo(moves)
    optimise_4_to_1(moves)
    optimise_3_to_1(moves)
    optimise_4_to_1(moves)
    optimise_half_turn_metric(moves)
    return moves