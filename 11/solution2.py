def process_seat(matrix, row, col):
    row_o = row
    col_o = col
    to_check = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]
    width = len(matrix[0]) - 1
    height = len(matrix) - 1
    c = 0
    for row_t, col_t in to_check:
        row += row_t
        col += col_t
        while 0 <= row <= height and 0 <= col <= width:
            if matrix[row][col] == '#':
                c += 1
                break
            elif matrix[row][col] == 'L':
                break
            row += row_t
            col += col_t
        row = row_o
        col = col_o
        if c == 5:
            break
    if c >= 5:
        return 'L'
    elif c == 0:
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
    # t = transform_matrix(transform_matrix(matrix))
    # for row in t:
    #     for col in row:
    #         print(col, end='')
    #     print('')
