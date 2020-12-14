if __name__ == '__main__':
    with open('input0', 'r') as file:
        start = int(file.readline().strip())
        departs = [int(i) if i.isdigit() else False for i in file.readline().split(',')]
    schedule = {}
    for idx, d in enumerate(departs):
        if d:
            schedule[d] = idx
    depart_offset = start % len(departs)
    bus = min({k: v for k, v in schedule.items() if v >= depart_offset}, key=schedule.get)
    depart = departs.index(bus)
    print(bus)
    print(depart)
    print(bus * (depart_offset % depart))
