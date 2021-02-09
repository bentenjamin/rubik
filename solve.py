import cube

Right = {
    "R":"B",
    "L":"F",
    "F":"R",
    "B":"L",
    "R'":"B'",
    "L'":"F'",
    "F'":"R'",
    "B'":"L'",
    "R2":"B2",
    "L2":"F2",
    "F2":"R2",
    "B2":"L2",
}

Left = {
    "L":"B",
    "R":"F",
    "F":"L",
    "B":"R",
    "L'":"B'",
    "R'":"F'",
    "F'":"L'",
    "B'":"R'",
    "L2":"B2",
    "R2":"F2",
    "F2":"L2",
    "B2":"R2",
}

Back = {
    "R":"L",
    "L":"R",
    "F":"B",
    "B":"F",
    "R'":"L'",
    "L'":"R'",
    "F'":"B'",
    "B'":"F'",
    "R2":"L2",
    "L2":"R2",
    "F2":"B2",
    "B2":"F2",
}

#up and down not included here
def move_translator(face, move):
    if face == "F":
        return move
    if face == "L":
        move = Left[move]
        return move
    if face == "R":
        move = Right[move]
        return move
    if face == "B":
        move = Back[move]
        return move

print(move_translator("L", "R'"))