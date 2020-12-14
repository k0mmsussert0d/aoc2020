if __name__ == '__main__':
    with open('input1', 'r') as file:
        file.readline()
        departs = [int(i) if i.isdigit() else i for i in file.readline().split(',')]
    for start in range(23, 1000000000000000, 23):
        print(start)
        offset = start
        for idx, depart in enumerate(departs):
            if idx == 0:
                continue
            offset += 1
            if depart == 'x':
                continue
            elif isinstance(depart, int):
                if offset % depart != 0:
                    break
                elif idx == len(departs) - 1:
                    print(f'FOUND: {start}')
                print(f'{offset}\t{depart}:{offset+depart}')
