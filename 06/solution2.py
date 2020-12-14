def count_in_grp(g):
    p = g.split('\n')
    return len(set(p[0]).intersection(*p))


if __name__ == '__main__':
    with open('input1', 'r') as file:
        f = file.read()

    groups = f.split('\n\n')
    print(sum([count_in_grp(i) for i in groups]))
