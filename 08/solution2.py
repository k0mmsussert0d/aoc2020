def move(lines, p):
    i = 0
    acc = 0
    steps = []
    seen = set()
    while True:
        steps.append(i)
        if i >= len(lines):
            return acc
        if i in seen:
            return acc if p else False
        seen.add(i)
        if lines[i][0] == 'acc':
            acc += lines[i][1]
            i += 1
        elif lines[i][0] == 'jmp':
            i += lines[i][1]
        elif lines[i][0] == 'nop':
            i += 1


def permut(lines):
    for idx, line in enumerate(lines):
        if line[0] == 'jmp':
            prev = line[0]
            lines[idx][0] = 'nop'
            if acc := move(lines, False):
                return acc
            lines[idx][0] = prev
        elif line[0] == 'nop':
            prev = line[0]
            lines[idx][0] = 'jmp'
            if acc := move(lines, False):
                return acc
            lines[idx][0] = prev


if __name__ == '__main__':
    lines = []
    with open('input1', 'r') as file:
        for i in file.readlines():
            parts = i.split(' ')
            lines.append([parts[0], int(parts[1].strip())])
    print(move(lines, True))
    print(permut(lines))
