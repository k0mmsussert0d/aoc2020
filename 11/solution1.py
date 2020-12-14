def process_seat(matrix, row, col):
    to_check = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]

    if row == 0:
        to_check = list(filter(lambda args: args[0] != -1, to_check))
    if col == 0:
        to_check = list(filter(lambda args: args[1] != -1, to_check))
    if row == len(matrix) - 1:
        to_check = list(filter(lambda args: args[0] != 1, to_check))
    if col == len(matrix[0]) - 1:
        to_check = list(filter(lambda args: args[1] != 1, to_check))

    adjacent = [matrix[row+i][col+j] for i, j in to_check]
    occupied = adjacent.count('#')

    if occupied >= 4:
        return 'L'
    elif occupied == 0:
        return '#'
    else:
        return matrix[row][col]


def transform_matrix(matrix):
    new_matrix = []
    for row, row_v in enumerate(matrix):
        new_matrix.append([])
        for col, col_v in enumerate(matrix[row]):
            if matrix[row][col] != '.':
                new_matrix[row].append(process_seat(matrix, row, col))
            else:
                new_matrix[row].append('.')
    return new_matrix


if __name__ == '__main__':
    with open('input1', 'r') as file:
        matrix = [i.strip() for i in file.readlines()]
    c = 0
    while True:
        old_matrix = matrix
        matrix = transform_matrix(matrix)
        c += 1
        if old_matrix == matrix:
            break
    print(sum([seat == '#' for row in matrix for seat in row]))
