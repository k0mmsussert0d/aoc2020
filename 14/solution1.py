import re


def apply_mask(value, mask):
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    return value


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
            mem[address] = apply_mask(value, mask)
    print(sum([i for i in mem.values()]))
