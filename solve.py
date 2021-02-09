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

class Algos:

    # get the side of the correlated coords [x, z]
    coord_to_side = {
        (1, 0): "B",
        (0, 1): "L",
        (2, 1): "R",
        (1, 2): "F"
    }

    # colour to cooord: tuple of x and z of the face
    c_t_c = {
        "O": (1, 0),
        "G": (0, 1),
        "B": (2, 1),
        "R": (1, 2)
    }

    side_to_coord = {
        "B": (1, 0),
        "L": (0, 1),
        "R": (2, 1),
        "F": (1, 2)
    }

    side_colour = {
        "F": "R",
        "B": "O",
        "L": "G",
        "R": "B",
        "U": "W",
        "D": "Y"
    }

    # colour to side
    c_t_s = {
        "R": "F",
        "O": "B",
        "G": "L",
        "B": "R",
        "W": "U",
        "Y": "D"
    }
    
    def __init__(self, c):
        # self.cube = c
        self.c = c
        self.moves = []
    
    def cross(self):

        for colour in ["R", "B", "O", "G"]:
            cubie_coords, cubie = cube.find_cubie([colour, "W", "N"])

            # if cubie is on the white face
            if (cubie_coords[1] == 2):
                cube.exe_move(coord_to_side[(cubie_coords[0], cubie_coords[2])] + "2")
            # if cubie is in the middle
            if (cubie_coords[1] == 1):
                # this is borked need to find which face it is on
                cube.exe_move("F D F'")
            # change to use point
            center = c[(c_t_c[colour])[0]][1][(c_t_c[colour])[1]]
            # change to use point
            while not c[c_t_c[colour][0]][0][c_t_c[colour][1]] == cubie:
                cube.exe_move("D")
            if cubie.colours[1] == "W":
                cube.exe_move(c_t_s[colour] + "2")
            else:
                cube.translate(colour, "F' U' R U")

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

# print(move_translator("L", "R'"))