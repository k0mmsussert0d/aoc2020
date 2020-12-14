def decode_pass(p: str):
    row = int(p[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(p[7:].replace('L', '0').replace('R', '1'), 2)
    return row*8+col


if __name__ == '__main__':
    with open('input1', 'r') as file:
        b = file.readlines()
    l=[decode_pass(i) for i in b]
    l.sort()
    prev = 0
    for id in l:
        if prev == 0 or id == prev+1:
            prev = id
        else:
            print(id)
            break
