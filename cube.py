import array


class Cube:
    def __init__(self):
        self.cube = [[11, 12, 13, 14, 15, 16, 17, 18, 19],
                     [21, 22, 23, 24, 25, 26, 27, 28, 29],
                     [31, 32, 33, 34, 35, 36, 37, 38, 39],
                     [41, 42, 43, 44, 45, 46, 47, 48, 49],
                     [51, 52, 53, 54, 55, 56, 57, 58, 59],
                     [61, 62, 63, 64, 65, 66, 67, 68, 69]]

    def rot_face(self, face_index):
        c = self.cube

        temp_corner = c[face_index][0]
        c[face_index][0] = c[face_index][6]
        c[face_index][6] = c[face_index][8]
        c[face_index][8] = c[face_index][2]
        c[face_index][2] = temp_corner

        temp_edge = c[face_index][1]
        c[face_index][1] = c[face_index][3]
        c[face_index][3] = c[face_index][7]
        c[face_index][7] = c[face_index][5]
        c[face_index][5] = temp_edge

    def rot_face_prime(self, face_index):
        c = self.cube

        temp_corner = c[face_index][2]
        c[face_index][2] = c[face_index][8]
        c[face_index][8] = c[face_index][6]
        c[face_index][6] = c[face_index][0]
        c[face_index][0] = temp_corner

        temp_edge = c[face_index][5]
        c[face_index][5] = c[face_index][7]
        c[face_index][7] = c[face_index][3]
        c[face_index][3] = c[face_index][1]
        c[face_index][1] = temp_edge

    def f(self):
        self.rot_face(0)
        c = self.cube

        tempora = c[4][6]
        c[4][6] = c[3][8]
        c[3][8] = c[5][2]
        c[5][2] = c[1][0]
        c[1][0] = tempora

        tempora = c[4][7]
        c[4][7] = c[3][5]
        c[3][5] = c[5][1]
        c[5][1] = c[1][3]
        c[1][3] = tempora

        tempora = c[4][8]
        c[4][8] = c[3][2]
        c[3][2] = c[5][0]
        c[5][0] = c[1][6]
        c[1][6] = tempora

    def b(self):
        self.rot_face(2)
        c = self.cube

        tempora = c[4][2]
        c[4][2] = c[1][8]
        c[1][8] = c[5][6]
        c[5][6] = c[3][0]
        c[3][0] = tempora

        tempora = c[4][1]
        c[4][1] = c[1][5]
        c[1][5] = c[5][7]
        c[5][7] = c[3][3]
        c[3][3] = tempora

        tempora = c[4][0]
        c[4][0] = c[1][2]
        c[1][2] = c[5][8]
        c[5][8] = c[3][6]
        c[3][6] = tempora

    def u(self):
        self.rot_face(4)
        c = self.cube

        tempora = c[2][2]
        c[2][2] = c[3][2]
        c[3][2] = c[0][2]
        c[0][2] = c[1][2]
        c[1][2] = tempora

        tempora = c[2][1]
        c[2][1] = c[3][1]
        c[3][1] = c[0][1]
        c[0][1] = c[1][1]
        c[1][1] = tempora

        tempora = c[2][0]
        c[2][0] = c[3][0]
        c[3][0] = c[0][0]
        c[0][0] = c[1][0]
        c[1][0] = tempora

    def d(self):
        self.rot_face(5)
        c = self.cube

        tempora = c[0][6]
        c[0][6] = c[3][6]
        c[3][6] = c[2][6]
        c[2][6] = c[1][6]
        c[1][6] = tempora

        tempora = c[0][7]
        c[0][7] = c[3][7]
        c[3][7] = c[2][7]
        c[2][7] = c[1][7]
        c[1][7] = tempora

        tempora = c[0][8]
        c[0][8] = c[3][8]
        c[3][8] = c[2][8]
        c[2][8] = c[1][8]
        c[1][8] = tempora

    def l(self):
        self.rot_face(3)
        c = self.cube

        tempora = c[4][0]
        c[4][0] = c[2][8]
        c[2][8] = c[5][0]
        c[5][0] = c[0][0]
        c[0][0] = tempora

        tempora = c[4][3]
        c[4][3] = c[2][5]
        c[2][5] = c[5][3]
        c[5][3] = c[0][3]
        c[0][3] = tempora

        tempora = c[4][6]
        c[4][6] = c[2][2]
        c[2][2] = c[5][6]
        c[5][6] = c[0][6]
        c[0][6] = tempora

    def r(self):
        self.rot_face(1)
        c = self.cube

        tempora = c[4][8]
        c[4][8] = c[0][8]
        c[0][8] = c[5][8]
        c[5][8] = c[2][0]
        c[2][0] = tempora

        tempora = c[4][5]
        c[4][5] = c[0][5]
        c[0][5] = c[5][5]
        c[5][5] = c[2][3]
        c[2][3] = tempora

        tempora = c[4][2]
        c[4][2] = c[0][2]
        c[0][2] = c[5][2]
        c[5][2] = c[2][6]
        c[2][6] = tempora

    def two_f(self):
        self.f()
        self.f()

    def two_b(self):
        self.b()
        self.b()

    def two_u(self):
        self.u()
        self.u()

    def two_d(self):
        self.d()
        self.d()

    def two_l(self):
        self.l()
        self.l()

    def two_r(self):
        self.r()
        self.r()

    def f_prime(self):
        self.rot_face_prime(0)
        c = self.cube

        tempora = c[1][0]
        c[1][0] = c[5][2]
        c[5][2] = c[3][8]
        c[3][8] = c[4][6]
        c[4][6] = tempora

        tempora = c[1][3]
        c[1][3] = c[5][1]
        c[5][1] = c[3][5]
        c[3][5] = c[4][7]
        c[4][7] = tempora

        tempora = c[1][6]
        c[1][6] = c[5][0]
        c[5][0] = c[3][2]
        c[3][2] = c[4][8]
        c[4][8] = tempora

    def b_prime(self):
        self.rot_face_prime(2)
        c = self.cube

        tempora = c[3][0]
        c[3][0] = c[5][6]
        c[5][6] = c[1][8]
        c[1][8] = c[4][2]
        c[4][2] = tempora

        tempora = c[3][3]
        c[3][3] = c[5][7]
        c[5][7] = c[1][5]
        c[1][5] = c[4][1]
        c[4][1] = tempora

        tempora = c[3][6]
        c[3][6] = c[5][8]
        c[5][8] = c[1][2]
        c[1][2] = c[4][0]
        c[4][0] = tempora

    def u_prime(self):
        self.rot_face_prime(4)
        c = self.cube

        tempora = c[1][2]
        c[1][2] = c[0][2]
        c[0][2] = c[3][2]
        c[3][2] = c[2][2]
        c[2][2] = tempora

        tempora = c[1][1]
        c[1][1] = c[0][1]
        c[0][1] = c[3][1]
        c[3][1] = c[2][1]
        c[2][1] = tempora

        tempora = c[1][0]
        c[1][0] = c[0][0]
        c[0][0] = c[3][0]
        c[3][0] = c[2][0]
        c[2][0] = tempora

    def d_prime(self):
        self.rot_face_prime(5)
        c = self.cube

        tempora = c[1][6]
        c[1][6] = c[2][6]
        c[2][6] = c[3][6]
        c[3][6] = c[0][6]
        c[0][6] = tempora

        tempora = c[1][7]
        c[1][7] = c[2][7]
        c[2][7] = c[3][7]
        c[3][7] = c[0][7]
        c[0][7] = tempora

        tempora = c[1][8]
        c[1][8] = c[2][8]
        c[2][8] = c[3][8]
        c[3][8] = c[0][8]
        c[0][8] = tempora
# here

    def l_prime(self):
        self.rot_face_prime(3)
        c = self.cube

        tempora = c[4][0]
        c[4][0] = c[2][8]
        c[2][8] = c[5][0]
        c[5][0] = c[0][0]
        c[0][0] = tempora

        tempora = c[4][3]
        c[4][3] = c[2][5]
        c[2][5] = c[5][3]
        c[5][3] = c[0][3]
        c[0][3] = tempora

        tempora = c[4][6]
        c[4][6] = c[2][2]
        c[2][2] = c[5][6]
        c[5][6] = c[0][6]
        c[0][6] = tempora

    def r_prime(self):
        self.rot_face_prime(1)
        c = self.cube

        tempora = c[4][8]
        c[4][8] = c[0][8]
        c[0][8] = c[5][8]
        c[5][8] = c[2][0]
        c[2][0] = tempora

        tempora = c[4][5]
        c[4][5] = c[0][5]
        c[0][5] = c[5][5]
        c[5][5] = c[2][3]
        c[2][3] = tempora

        tempora = c[4][2]
        c[4][2] = c[0][2]
        c[0][2] = c[5][2]
        c[5][2] = c[2][6]
        c[2][6] = tempora

    def print_cube(self):
        cube = self.cube
        print(f"           {cube[4][0]} {cube[4][1]} {cube[4][2]}")
        print(f"           {cube[4][3]} {cube[4][4]} {cube[4][5]}")
        print(f"           {cube[4][6]} {cube[4][7]} {cube[4][8]}")
        print(f"{cube[3][0]} {cube[3][1]} {cube[3][2]}   {cube[0][0]} {cube[0][1]} {cube[0][2]}   {cube[1][0]} {cube[1][1]} {cube[1][2]}   {cube[2][0]} {cube[2][1]} {cube[2][2]}")
        print(f"{cube[3][3]} {cube[3][4]} {cube[3][5]}   {cube[0][3]} {cube[0][4]} {cube[0][5]}   {cube[1][3]} {cube[1][4]} {cube[1][5]}   {cube[2][3]} {cube[2][4]} {cube[2][5]}")
        print(f"{cube[3][6]} {cube[3][7]} {cube[3][8]}   {cube[0][6]} {cube[0][7]} {cube[0][8]}   {cube[1][6]} {cube[1][7]} {cube[1][8]}   {cube[2][6]} {cube[2][7]} {cube[2][8]}")
        print(f"           {cube[5][0]} {cube[5][1]} {cube[5][2]}")
        print(f"           {cube[5][3]} {cube[5][4]} {cube[5][5]}")
        print(f"           {cube[5][6]} {cube[5][7]} {cube[5][8]}")


cube = Cube()
cube.d_prime()
cube.print_cube()
