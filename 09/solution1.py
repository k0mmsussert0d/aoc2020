def get_amble(idx, lines):
    return lines[idx-25:idx]


def get_pair(idx, lines):
    amble = get_amble(idx, lines)
    for i in amble:
        for j in amble:
            if i > lines[idx] or j > lines[idx]:
                continue
            if i == j:
                continue
            if i + j == lines[idx]:
                return i, j


def find_series(idx, lines):
    target = lines[idx]
    for i in range(idx - 1, 0, -1):
        for j in range(i - 2, -1, -1):
            s = lines[i:j:-1]
            if any([i > target for i in s]):
                break
            if sum(s) == target:
                return s


if __name__ == '__main__':
    with open('input0', 'r') as file:
        lines = [int(i.strip()) for i in file.readlines()]

    # for i in range(25, 1000):
    #     if pair := get_pair(i, lines):
    #         print(pair)
    #     else:
    #         print('STOP')
    #         print(i)
    #         print(lines[i])
    #         break

    series = find_series(511, lines)
    print(min(series) + max(series))
