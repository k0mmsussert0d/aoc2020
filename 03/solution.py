def traverse(map, step_x, step_y):
    height = len(map)
    single_width = len(map[0])

    extend_y = (step_x * height) // single_width + 1
    map = [extend_y * row for row in map]

    width = single_width * extend_y

    x = y = c = 0
    while y < height and x < width:
        if map[y][x] == '#':
            c += 1
        x += step_x
        y += step_y
    print(c)
    return c


if __name__ == '__main__':
    map = []
    with open('input1', 'r') as file:
        map = file.readlines()

    map = [n.replace('\n', '') for n in map]

    print(traverse(map, 1, 1) * traverse(map, 3, 1) * traverse(map, 5, 1) * traverse(map, 7, 1) * traverse(map, 1, 2))
