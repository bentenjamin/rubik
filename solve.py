import helper
import cube
from cube import np

#dicts for translating moves relative to front face
Right = {
    "D": "D",
    "U": "U",
    "D'": "D'",
    "U'": "U'",
    "D2": "D2",
    "U2": "U2",
    "R": "B",
    "L": "F",
    "F": "R",
    "B": "L",
    "R'": "B'",
    "L'": "F'",
    "F'": "R'",
    "B'": "L'",
    "R2": "B2",
    "L2": "F2",
    "F2": "R2",
    "B2": "L2",
}

Left = {
    "D": "D",
    "U": "U",
    "D'": "D'",
    "U'": "U'",
    "D2": "D2",
    "U2": "U2",
    "L": "B",
    "R": "F",
    "F": "L",
    "B": "R",
    "L'": "B'",
    "R'": "F'",
    "F'": "L'",
    "B'": "R'",
    "L2": "B2",
    "R2": "F2",
    "F2": "L2",
    "B2": "R2",
}

Back = {
    "D": "D",
    "U": "U",
    "D'": "D'",
    "U'": "U'",
    "D2": "D2",
    "U2": "U2",
    "R": "L",
    "L": "R",
    "F": "B",
    "B": "F",
    "R'": "L'",
    "L'": "R'",
    "F'": "B'",
    "B'": "F'",
    "R2": "L2",
    "L2": "R2",
    "F2": "B2",
    "B2": "F2",
}


class Algos:
    # dict for getting the the face left or right of a piece in a corner
    lor_face_of_col = {
        (0, 0, "l"): "O",
        (0, 0, "r"): "G",
        (0, 2, "l"): "G",
        (0, 2, "r"): "R",
        (2, 0, "l"): "B",
        (2, 0, "r"): "O",
        (2, 2, "l"): "R",
        (2, 2, "r"): "B"
    }

    #constructor to setup cube and moves and determine if debug needed
    def __init__(self, cube):
        self.cube = cube
        self.c = cube.cube
        self.moves = []
        self.debug = cube.debug

    # get the colour that isnt N (for NULL) 
    def get_center_colour(self, cubie):
        return [x for x in cubie.colours if x not in "N"][0]

    def get_edge_colour(self, cubie):
        return [x for x in cubie.colours if x not in "NWY"][0]

    def get_other_colour(self, cubie, exclude):
        return [x for x in cubie.colours if x not in "N" + exclude][0]

    #adds the moves to solve the cube to a list and executes the moves on the cube.
    def write_exe_moves(self, moves):
        self.moves.extend(moves)
        self.cube.do_moves(moves)
        if self.debug == True:
            print(*moves)
            print(self.cube)

    #solves the first step: the white cross
    def cross(self):
        c = self.c

        # iterate through all the white edges
        for x, z in [(1, 0), (0, 1), (2, 1), (1, 2)]:
            cubie = self.cube.pieces[x][2][z]

            # if cubie is on the white face
            if (cubie.point[1] == 2):
                # skip if its in the right place
                if (cubie.colours[1] == "W") and (self.c[x][2][z] is cubie):
                    continue
                # move out of the top
                self.write_exe_moves(
                    [move_translator(self.get_center_colour(self.c[cubie.point[0]][1][cubie.point[2]]), ["F"])[0] + "2"])

            # if cubie is in the middle move it out
            if (cubie.point[1] == 1):
                self.write_exe_moves(move_translator(
                    self.lor_face_of_col[(cubie.point[0], cubie.point[2], "l")], ["F", "D", "F'"]))

            # move cubie to the right colour
            while self.get_edge_colour(cubie) != self.get_center_colour(self.c[cubie.point[0]][1][cubie.point[2]]):
                self.write_exe_moves(["D"])

            # different algo for different orientation
            if cubie.colours[1] == "W":
                self.write_exe_moves(
                    [move_translator(self.get_edge_colour(cubie), "F")[0] + "2"])
            else:
                self.write_exe_moves(move_translator(
                    self.get_edge_colour(cubie), "F' U' R U".split()))

    #helper function for white corners, executes the translated moves relative to the xz position of the cubie
    def white_corner_helper(self, x, z, moves):
        self.write_exe_moves(move_translator(
            self.lor_face_of_col[(x, z, "l")], moves))

    #solves the second step: the white corners on the white face
    def white_corners(self):
        for x in [0, 2]:
            for z in [0, 2]:
                cubie = self.cube.pieces[x][2][z]

                if cubie.point[1] == 2:
                    if (cubie.colours[1] == "W") and (self.cube.cube[x][2][z] is cubie):
                        continue
                    self.white_corner_helper(
                        cubie.point[0], cubie.point[2], ["R'", "D'", "R"])

                while not ((cubie.point[0] == x) and (cubie.point[2] == z)):
                    self.write_exe_moves(['D'])

                if cubie.colours[1] == "W":
                    self.white_corner_helper(x, z, ["R'", "D", "R", "D2"])

                if (cubie.colours[2] == "W" and x == z) or (cubie.colours[0] == "W" and x != z):
                    self.white_corner_helper(x, z, ["F", "D", "F'"])
                else:
                    self.white_corner_helper(x, z, ["R'", "D'", "R"])

    #third section to solve, the middle layer edges in the correct spots
    def middle_edges(self):
        ROT_XZ_CW = np.array([[0, 0, -1],
                              [0, 1, 0],
                              [1, 0, 0]])

        for x in [0, 2]:
            for z in [0, 2]:
                cubie = self.cube.pieces[x][1][z]

                if cubie.point[1] == 1:
                    # idk if this works
                    # if (self.c[x][2][z] is cubie) and (cubie.point[0] == self.c[1][1][z]):
                    #     continue
                    self.white_corner_helper(
                        cubie.point[0], cubie.point[2], ["R'", "D", "R", "D", "F", "D'", "F'"])

                # align cubie with centre
                while self.get_other_colour(cubie, cubie.colours[1]) != self.get_center_colour(self.c[cubie.point[0]][1][cubie.point[2]]):
                    self.write_exe_moves(['D'])

                # get point of center on the right of the current face
                rc = np.dot(
                    [cubie.point[0] - 1, 0, cubie.point[2] - 1], ROT_XZ_CW)

                # move edge into correct slot
                if cubie.colours[1] == self.get_center_colour(self.c[rc[0] + 1][1][rc[2] + 1]):
                    moves = ["D'", "R'", "D", "R", "D", "F", "D'", "F'"]
                else:
                    moves = ["D", "L", "D'", "L'", "D'", "F'", "D", "F"]
                self.write_exe_moves(move_translator(
                    self.get_other_colour(cubie, cubie.colours[1]), moves))

    #fourth step of the solve, the yellow cross on the bottom layer
    def yellow_cross(self):
        # check if the cross is already done
        if not (self.c[1][0][0].colours[1] == "Y" and self.c[1][0][2].colours[1] == "Y" and self.c[0][0][1].colours[1] == "Y" and self.c[2][0][1].colours[1] == "Y"):
            # check if there is a line
            if not (self.c[1][0][0].colours[1] == self.c[1][0][2].colours[1] or self.c[0][0][1].colours[1] == self.c[2][0][1].colours[1]):
                # check if its an L or dot
                if self.c[1][0][0].colours[1] == "Y" or self.c[1][0][2].colours[1] == "Y":
                    # orientate L
                    while not (self.c[1][0][0].colours[1] == "Y" and self.c[2][0][1].colours[1] == "Y"):
                        self.write_exe_moves(["D"])
                # L -> cross, or dot to line
                self.write_exe_moves(
                    ["F", "L", "D", "L'", "D'", "L", "D", "L'", "D'", "F'", "D"])
            # orientate line
            elif self.c[1][0][2].colours[1] == "Y":
                self.write_exe_moves(["D"])

            # if line make cross
            if self.c[1][0][2].colours[1] != "Y":
                self.write_exe_moves(["F", "L", "D", "L'", "D'", "F'"])

    #5th step, make sure the yellow edges are in the correct spots
    def yellow_edges(self):
        opposite_colour = {
            "O": "R",
            "R": "O",
            "B": "G",
            "G": "B"
        }
        adj_colour = {
            "O": "B",
            "R": "G",
            "B": "R",
            "G": "O"
        }

        # check if its already correct
        if not (opposite_colour[self.c[1][0][0].colours[2]] == self.c[1][0][2].colours[2] and adj_colour[self.c[1][0][2].colours[2]] == self.c[1][0][2].colours[2]):
            #check if there is one pair of opposites
            if (opposite_colour[self.c[1][0][0].colours[2]] == self.c[1][0][2].colours[2] or opposite_colour[self.c[0][0][1].colours[0]] == self.c[2][0][1].colours[0]):
                # orientate opposites
                if opposite_colour[self.c[0][0][1].colours[0]] == self.c[2][0][1].colours[0]:
                    self.write_exe_moves(["D"])
                # line -> L
                self.write_exe_moves(
                    ["L", "D", "L'", "D", "L", "D", "D", "L'"])

            # orientate L
            while adj_colour[self.c[0][0][1].colours[0]] != self.c[1][0][0].colours[2]:
                self.write_exe_moves(["D"])
            
            # L to edges
            self.write_exe_moves(["L", "D", "L'", "D", "L", "D", "D", "L'"])

            # line up edges, unneccesary but looks good
            while self.c[1][1][2].colours[2] != self.c[1][0][2].colours[2]:
                self.write_exe_moves(["D"])

    #check to see if the yellow corners are in the correct spot 
    def check_yellow_corners(self):
        yes_cubies = []
        for x in [0, 2]:
            for z in [0, 2]:
                if self.get_center_colour(self.c[x][1][1]) in self.c[x][0][z].colours and self.get_center_colour(self.c[1][1][z]) in self.c[x][0][z].colours:
                    yes_cubies.append((x, z))

        return yes_cubies

    #6th step in solve, moves the yellow cubies to the correct positions
    def yellow_corner_setup(self):

        correct_cubies = self.check_yellow_corners()

        # reorder corners until they are in the right place
        while len(correct_cubies) != 4:
            self.write_exe_moves(move_translator(self.lor_face_of_col[correct_cubies[0][0], correct_cubies[0][1], "l"] if len(
                correct_cubies) == 1 else "F", ["D'", "R'", "D", "L", "D'", "R", "D", "L'"]))
            correct_cubies = self.check_yellow_corners()

    #7th step in solve, makes sure yellow cubies are in the correct orientation
    def yellow_corner_rot(self):
        for i in range(4):
            while self.c[2][0][2].colours[1] != "Y":
                self.write_exe_moves(["R", "U", "R'", "U'"])
            self.write_exe_moves(["D"])

#translates moves from front face to other x/z faces using dicts
def move_translator(face, moves):
    new_moves = []
    for move in moves:
        if face == "R":
            new_moves.append(move)
        elif face == "G":
            move = Left[move]
            new_moves.append(move)
        elif face == "B":
            move = Right[move]
            new_moves.append(move)
        elif face == "O":
            move = Back[move]
            new_moves.append(move)
        else:
            new_moves.append(move)
    return(new_moves)

#calls all the solving algorithms to solve the vrious stages of the cube
def solve(cube):
    if cube.is_solved():
        return ([])
    algos = Algos(cube)

    algos.cross()
    algos.white_corners()
    algos.middle_edges()
    algos.yellow_cross()
    algos.yellow_edges()
    algos.yellow_corner_setup()
    algos.yellow_corner_rot()

    algos.moves = helper.optimise_all(algos.moves)
    return (algos.moves)