from collections import defaultdict


def remove_and_check(l: list):
    paths = defaultdict(int)
    paths[0] = 1
    for i in l:
        for diff in range(1, 4):
            n = i + diff
            if n in l:
                paths[n] += paths[i]
    return paths[l[len(l)-1]]


if __name__ == '__main__':
    with open('input1', 'r') as file:
        l = [int(i.strip()) for i in file.readlines()]
    l.sort()
    l.insert(0, 0)
    l.append(l[len(l) - 1] + 3)
    print(remove_and_check(l))
