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


def bag_contains(x):
    count = 0
    big_bag = d.get(x)
    for bag_name, bags_count in big_bag.items():
        count += bags_count
        count += bag_contains(bag_name) * bags_count
    return count


if __name__ == '__main__':
    with open('input1', 'r') as file:
        f = file.readlines()
    [process_line(l) for l in f]
    print(bag_contains('shiny gold'))
