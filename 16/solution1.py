def matches_rule(val, rule):
    return any([p[0] <= val <= p[1] for p in rule])


if __name__ == '__main__':
    with open('./input1', 'r') as f:
        req = {}
        while (line := f.readline()) != '\n':
            parts = line.split(': ')
            for x in parts[1].split(' or '):
                y = x.strip().split('-')
                if req.get(parts[0]):
                    req[parts[0]].append((int(y[0]), int(y[1])))
                else:
                    req[parts[0]] = [(int(y[0]), int(y[1]))]
        f.readline()  # your ticket:
        your_ticket = [int(x.strip()) for x in f.readline().split(',')]
        f.readline()  # \n
        f.readline()  # nearby tickets:
        nearby_tickets = []
        while line := f.readline():
            nearby_tickets.append([int(x.strip()) for x in line.split(',')])

    wrong = []
    for ticket in nearby_tickets:
        for num in ticket:
            if not any([matches_rule(num, rule) for rule in req.values()]):
                wrong.append(num)
    print(sum(wrong))
