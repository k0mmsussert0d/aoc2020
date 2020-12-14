import re


d = {}


def process_line(line):
    g = re.search(r'^(.+) bags contain (.+).$', line)
    parent = g.group(1)
    if g.group(2) == 'no other bags':
        children = {}
    else:
        children = {
            typ: int(count) for count, typ in
            [re.search(r'^(\d) (.+)$', j).groups() for j in
                [i.replace('bags', '').replace('bag', '').replace('.', '').strip() for i in g.group(2).split(',')]]
            }
    d[parent] = children


def bags_containing_x(x):
    res = set()
    for bag_name, bags in d.items():
        if x in bags:
            res.add(bag_name)
            res |= bags_containing_x(bag_name)
    return res


if __name__ == '__main__':
    with open('input1', 'r') as file:
        f = file.readlines()
    [process_line(l) for l in f]
    print(len(bags_containing_x('shiny gold')))
