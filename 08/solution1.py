if __name__ == '__main__':
    lines = []
    with open('input1', 'r') as file:
        for i in file.readlines():
            parts = i.split(' ')
            lines.append([parts[0], int(parts[1].strip()), False])

    i = 0
    acc = 0
    while lines[i][2] is not True:
        print(lines[i], i)
        lines[i][2] = True
        if lines[i][0] == 'acc':
            acc += lines[i][1]
            i += 1
        elif lines[i][0] == 'jmp':
            i += lines[i][1]
        elif lines[i][0] == 'nop':
            i += 1
    print(acc)
