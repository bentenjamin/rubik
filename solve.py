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
    
    def __init__(self, cube):
        # self.cube = c
        self.cube = cube
        self.c = cube.cube
        self.moves = []

    def write_exe_moves(self, moves):
        self.moves.append(moves)
        self.cube.do_moves(moves)
    
    def cross(self):
        mid_layer_white_edge = {
            (0, 0): "O",
            (0, 2): "G",
            (2, 0): "B",
            (2, 2): "R"
        }

        for colour in ["R", "B", "O", "G"]:
            cubie = cube.find_cubie([colour, "W", "N"])

            # if cubie is on the white face
            if (cubie.point[1] == 2):
                self.write_exe_moves(colour, coord_to_side[(cubie.point[0], cubie.point[2])] + "2")
            # if cubie is in the middle
            if (cubie.point[1] == 1):
                # this is borked need to find which face it is on
                self.write_exe_moves(move_translator(mid_layer_white_edge[(cubie.point[0], cubie.point[2])], "F D F'"))
            # change to use point
            center = c[(c_t_c[colour])[0]][1][(c_t_c[colour])[1]]
            # change to use point
            while not c[c_t_c[colour][0]][0][c_t_c[colour][1]] == cubie:
                self.write_exe_moves("D")
            if cubie.colours[1] == "W":
                self.write_exe_moves(c_t_s[colour] + "2")
            else:
                self.write_exe_moves(colour, "F' U' R U")

#up and down not included here
def move_translator(face, moves):
    new_moves = []
    for move in moves:
        if face == "R":
            new_moves.append(move)
        if face == "G":
            move = Left[move]
            new_moves.append(move)
        if face == "B":
            move = Right[move]
            new_moves.append(move)
        if face == "O":
            move = Back[move]
            new_moves.append(move)
    return(new_moves)

# print(move_translator("L", "R'"))