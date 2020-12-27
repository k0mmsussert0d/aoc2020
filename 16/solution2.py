import functools
import itertools
import operator


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
    ok = []
    for ticket in nearby_tickets:
        for num in ticket:
            if not any([matches_rule(num, rule) for rule in req.values()]):
                wrong.append(ticket)

    ok = [x for x in nearby_tickets if x not in wrong]
    ok.append(your_ticket)

    mappings = []

    for i in range(len(ok[0])):
        m = []
        for r_name, rule in req.items():
            if all([matches_rule(ticket[i], rule) for ticket in ok]):
                m.append(r_name)
        mappings.append(m)

    mappings = list(enumerate(mappings))

    mappings.sort(key=lambda args: len(args[1]))
    for idx, fields in enumerate(mappings):
        only_value = fields[1][0]
        for idx_2, next_fields in mappings[idx+1:]:
            next_fields.remove(only_value)

    mappings.sort(key=lambda args: args[0])
    mappings = list(map(lambda args: args[1][0], mappings))

    print(functools.reduce(operator.mul, list(map(lambda x: x[1], filter(lambda args: mappings[args[0]].startswith('departure'), enumerate(your_ticket))))))
