#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tot_matrix = []
    for i in range(len(matrix)):
        seq = matrix[i]
        new_matrix = map(lambda a: a * a, matrix[i])
        tot_matrix.append(list(new_matrix))
    return tot_matrix


if __name__ == '__main__':
    square_matrix_simple(matrix=[])
