if __name__ == '__main__':
    with open('input1', 'r') as file:
        l = [int(i.strip()) for i in file.readlines()]
    l.sort()
    l.insert(0, 0)
    l.append(l[len(l)-1] + 3)
    diffs = [b - a for a, b in zip(l, l[1:])]
    print(diffs.count(1) * diffs.count(3))
