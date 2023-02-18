# Matrix Rotations

# You are given a square matrix A of dimensions NxN. You need to apply the below given 3 operations on the matrix A.

from copy import deepcopy


def rotate90_clockwise(mat):
    return [list(reversed(col)) for col in zip(*mat)]


def rotate(mat, _angle):
    _angle = _angle % 360 // 90
    for _ in range(_angle):
        mat = rotate90_clockwise(mat)
    return mat


def update(mat, rot_list, _args):
    i, j, value = map(int, _args)
    mat[i][j] = str(value)
    mat = rotate(mat, sum(rot_list))
    return mat


def query(mat, _args):
    i, j = map(int, _args)
    print(mat[i][j])


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(
            list(input().split())
        )
    handle = ""
    rotation_list = []
    initial_matrix = deepcopy(matrix)
    while handle != "-1":
        handle, *args = input().split()
        if handle == "R":
            angle = int(args[0])
            rotation_list.append(angle)
            matrix = rotate(matrix, angle)
        elif handle == "U":
            matrix = update(deepcopy(initial_matrix), rotation_list, args)
        elif handle == "Q":
            query(matrix, args)


# Coding Solutions Youtube Channel
