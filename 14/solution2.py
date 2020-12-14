import re
import itertools


def get_addresses(mask: str, address: int):
    address |= int(mask.replace('X', '0'), 2)
    floatings = itertools.product('01', repeat=mask.count('X'))
    res = []
    for f in floatings:
        c = 0
        s = []
        for idx, j in enumerate(mask):
            if j == 'X':
                s.append(f[c])
                c += 1
            else:
                s.append(bin(address).lstrip('0b').zfill(36)[idx])
        res.append(''.join(s))
    return res


if __name__ == '__main__':
    with open('input1', 'r') as file:
        ins = file.readlines()
    mask = ''
    mem = {}
    for i in ins:
        if i.startswith('mask'):
            mask = re.search(r'^mask = ([0-1X]+)$', i).group(1)
        elif i.startswith('mem'):
            line = re.search(r'^mem\[(\d+)] = (\d+)$', i)
            address = line.group(1)
            value = int(line.group(2))
            addresses = get_addresses(mask, int(address))
            for a in addresses:
                mem[a] = value
    print(sum([i for i in mem.values()]))
