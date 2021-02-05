import numpy as np

# 90 degree rotations in the XY plane. CW is clockwise, CC is counter-clockwise.
ROT_XY_CW = np.array([[0, 1, 0],
                      [-1, 0, 0],
                      [0, 0, 1]])
ROT_XY_CC = np.array([[0, -1, 0],
                      [1, 0, 0],
                      [0, 0, 1]])

# 90 degree rotations in the XZ plane (around the y-axis when viewed pointing toward you).
ROT_XZ_CW = np.array([[0, 0, -1],
                      [0, 1, 0],
                      [1, 0, 0]])
ROT_XZ_CC = np.array([[0, 0, 1],
                      [0, 1, 0],
                      [-1, 0, 0]])

# 90 degree rotations in the YZ plane (around the x-axis when viewed pointing toward you).
ROT_YZ_CW = np.array([[1, 0, 0],
                      [0, 0, 1],
                      [0, -1, 0]])
ROT_YZ_CC = np.array([[1, 0, 0],
                      [0, 0, -1],
                      [0, 1, 0]])


class Cube:
    # F, B, L, R, U, D
    # 0 null, 1 red, 2 orange, 3 green, 4 blue, 5 white, 6 yellow

    cube = [[[0 for z in range(3)] for y in range(3)] for x in range(3)]

    def __init__(self):
        c = self.cube
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    colours = [0, 0, 0]
                    colours[0] = 'G' if x == 0 else 'B' if x == 2 else 'N'
                    colours[1] = 'Y' if y == 0 else 'W' if y == 2 else 'N'
                    colours[2] = 'O' if z == 0 else 'R' if z == 2 else 'N'
                    self.cube[x][y][z] = Cubie(colours)

    def get_face(self, xrng, yrng, zrng, face):
        c = self.cube

        out = ['N' for x in range(9)]
        i = 0
        for x in xrng:
            for y in yrng:
                for z in zrng:
                    out[i] = self.cube[x][y][z].colours[face]
                    i += 1
        return out

    def print_up(self):
        string = ''
        c = self.cube
        for z in range(3):
            string += "       "
            for x in range(3):
                string += f"{c[x][2][z].colours[1]} "
            string += "\n"

        print(string)

    def __str__(self):
        c = self.cube
        string = f"""
                {c[0][2][0].colours[1]} {c[1][2][0].colours[1]} {c[2][2][0].colours[1]}
                {c[0][2][1].colours[1]} {c[1][2][1].colours[1]} {c[2][2][1].colours[1]}
                {c[0][2][2].colours[1]} {c[1][2][2].colours[1]} {c[2][2][2].colours[1]}
        {c[0][2][0].colours[0]} {c[0][2][1].colours[0]} {c[0][2][2].colours[0]}   {c[0][2][2].colours[2]} {c[1][2][2].colours[2]} {c[2][2][2].colours[2]}   {c[2][2][2].colours[0]} {c[2][2][1].colours[0]} {c[2][2][0].colours[0]}   {c[2][2][0].colours[2]} {c[1][2][0].colours[2]} {c[0][2][0].colours[2]}
        {c[0][1][0].colours[0]} {c[0][1][1].colours[0]} {c[0][1][2].colours[0]}   {c[0][1][2].colours[2]} {c[1][1][2].colours[2]} {c[2][1][2].colours[2]}   {c[2][1][2].colours[0]} {c[2][1][1].colours[0]} {c[2][1][0].colours[0]}   {c[2][1][0].colours[2]} {c[1][1][0].colours[2]} {c[0][1][0].colours[2]}
        {c[0][0][0].colours[0]} {c[0][0][1].colours[0]} {c[0][0][2].colours[0]}   {c[0][0][2].colours[2]} {c[1][0][2].colours[2]} {c[2][0][2].colours[2]}   {c[2][0][2].colours[0]} {c[2][0][1].colours[0]} {c[2][0][0].colours[0]}   {c[2][0][0].colours[2]} {c[1][0][0].colours[2]} {c[0][0][0].colours[2]}
                {c[0][0][2].colours[1]} {c[1][0][2].colours[1]} {c[2][0][2].colours[1]}
                {c[0][0][1].colours[1]} {c[1][0][1].colours[1]} {c[2][0][1].colours[1]}
                {c[0][0][0].colours[1]} {c[1][0][0].colours[1]} {c[2][0][0].colours[1]}"""
        return string

    def f(self):
        self.rot_face([2, 1, 0], [2, 1, 0], [2], ROT_XY_CC)
    
    def b(self):
        self.rot_face([0, 1, 2], [0, 1, 2], [0], ROT_XY_CW)

    def r(self):
        self.rot_face([2], [0, 1, 2], [0, 1, 2], ROT_YZ_CC)
    
    def l(self):
        self.rot_face([0], [0, 1, 2], [0, 1, 2], ROT_YZ_CW)

    def u(self):
        self.rot_face([0, 1, 2], [2], [0, 1, 2], ROT_XZ_CC)

    def d(self):
        self.rot_face([0, 1, 2], [0], [0, 1, 2], ROT_XZ_CW)

    def f_prime(self):
        self.rot_face([2, 1, 0], [2, 1, 0], [2], ROT_XY_CW)
    
    def b_prime(self):
        self.rot_face([0, 1, 2], [0, 1, 2], [0], ROT_XY_CC)

    def r_prime(self):
        self.rot_face([2], [0, 1, 2], [0, 1, 2], ROT_YZ_CW)
    
    def l_prime(self):
        self.rot_face([0], [0, 1, 2], [0, 1, 2], ROT_YZ_CC)

    def u_prime(self):
        self.rot_face([0, 1, 2], [2], [0, 1, 2], ROT_XZ_CW)

    def d_prime(self):
        self.rot_face([0, 1, 2], [0], [0, 1, 2], ROT_XZ_CC)

    def two_f(self):
        for i in range(2):
            self.f()
    
    def two_b(self):
        for i in range(2):
            self.b()

    def two_r(self):
        for i in range(2):
            self.r()
    
    def two_l(self):
        for i in range(2):
            self.l()

    def two_u(self):
        for i in range(2):
            self.u()

    def two_d(self):
        for i in range(2):
            self.d()

    def get_colour_indexs(self, lists):
        colours = []

        for i in range(3):
            if len(lists[i]) > 1:
                colours.append(i)

        return colours

    def rot_face(self, xrng, yrng, zrng, rot_matrix):
        c = self.cube

        c_i = self.get_colour_indexs([xrng, yrng, zrng])

        trans = [[[0 for z in range(3)] for y in range(3)] for x in range(3)]
        for x in xrng:
            for y in yrng:
                for z in zrng:
                    matrix = np.dot([x - 1, y - 1, z - 1], rot_matrix)
                    matrix = [matrix[0] + 1, matrix[1] + 1, matrix[2] + 1]
                    trans[matrix[0]][matrix[1]][matrix[2]] = c[x][y][z]

                    tc = trans[matrix[0]][matrix[1]][matrix[2]].colours
                    tc[c_i[0]], tc[c_i[1]] = tc[c_i[1]], tc[c_i[0]]
        for x in xrng:
            for y in yrng:
                for z in zrng:
                    c[x][y][z] = trans[x][y][z]


class Cubie:
    # x face y face z face colours
    colours = ['N' for x in range(3)]

    def __init__(self, colours):
        self.colours = colours

    def print_me(self):
        string = ''
        for x in self.colours:
            string += x
        return string


cube = Cube()
# cube.print_me()
# print(cube.get_face([0, 1, 2], [2], [0, 1, 2], 1))
cube.two_u()
print(cube)
