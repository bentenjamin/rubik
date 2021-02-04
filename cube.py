import numpy

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

    def __init__(self, colours):
        self.colours = colours
    
    def print_me(self):
        string  = ''
        for x in self.colours:
            string += x
        return string

cube = Cube()
# cube.print_me()
# print(cube.get_face([0, 1, 2], [2], [0, 1, 2], 1))
print(cube)
