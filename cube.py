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
                    point = [x - 1, y - 1, z - 1]
                    self.cube[x][y][z] = Cubie(colours, point)

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
        
    def rotate_face(self, xrng, yrng, zrng, rot_matrix):
        c = self.cube

        #get cubies to be rotated in the face
        indices = []
        i = 0
        for x in xrng:
            for y in yrng:
                for z in zrng:
                    indices.append(self.cube[x][y][z])

        #applies matrix to cubie location and rotates pieces (not colours)
        for cubie in indices:
            cubie.point = np.dot(cubie.point, rot_matrix)
        
        #stores changed cubies back into original cube
        for cubie in indices:
            self.cube[cubie.point[0]][cubie.point[1]][cubie.point[2]] = cubie

    def f(self):
        self.rotate_face([0, 1, 2], [0, 1, 2], [2], ROT_XY_CW)

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
                {c[0][2][2].colours[1]} {c[1][2][2].colours[1]} {c[2][2][1].colours[1]}
        {c[0][2][0].colours[0]} {c[0][2][1].colours[0]} {c[0][2][2].colours[0]}   {c[0][2][2].colours[2]} {c[1][2][2].colours[2]} {c[2][2][2].colours[2]}   {c[2][2][2].colours[0]} {c[2][2][1].colours[0]} {c[2][2][0].colours[0]}   {c[2][2][0].colours[2]} {c[1][2][0].colours[2]} {c[0][2][0].colours[2]}
        {c[0][1][0].colours[0]} {c[0][1][1].colours[0]} {c[0][1][2].colours[0]}   {c[0][1][2].colours[2]} {c[1][1][2].colours[2]} {c[2][1][2].colours[2]}   {c[2][1][2].colours[0]} {c[2][1][1].colours[0]} {c[2][1][0].colours[0]}   {c[2][1][0].colours[2]} {c[1][1][0].colours[2]} {c[0][1][0].colours[2]}
        {c[0][0][0].colours[0]} {c[0][0][1].colours[0]} {c[0][0][2].colours[0]}   {c[0][0][2].colours[2]} {c[1][0][2].colours[2]} {c[2][0][2].colours[2]}   {c[2][0][2].colours[0]} {c[2][0][1].colours[0]} {c[2][0][0].colours[0]}   {c[2][0][0].colours[2]} {c[1][0][0].colours[2]} {c[0][0][0].colours[2]}
                {c[0][0][2].colours[1]} {c[1][0][2].colours[1]} {c[2][0][2].colours[1]}
                {c[0][0][1].colours[1]} {c[1][0][1].colours[1]} {c[2][0][1].colours[1]}
                {c[0][0][0].colours[1]} {c[1][0][0].colours[1]} {c[2][0][0].colours[1]}"""
        return string
    
class Cubie:
    # x face y face z face colours
    colours = ['N' for x in range(3)]

    def __init__(self, colours, point):
        self.colours = colours
        self.point = point
    
    def print_me(self):
        string  = ''
        for x in self.colours:
            string += x
        return string

cube = Cube()
# cube.print_me()
# print(cube.get_face([0, 1, 2], [2], [0, 1, 2], 1))
# point = ([1, 1, -1])
# product = np.dot(ROT_YZ_CW, point)
# print(product)
print(cube)
cube.f()
print(cube)
