import re


class Ship:
    def __init__(self, dirr):
        self._dirs = ['N', 'E', 'S', 'W']
        self._dir = dirr
        self._ns = 0
        self._ew = 0

    def sail_in_direction(self, dirr, steps):
        if dirr == 'N':
            self._ns += steps
        elif dirr == 'S':
            self._ns -= steps
        elif dirr == 'W':
            self._ew -= steps
        elif dirr == 'E':
            self._ew += steps
        else:
            raise AssertionError(f'Unexpected direction {dirr}')

    def sail_forward(self, steps):
        self.sail_in_direction(self._dir, steps)

    def rotate_left(self, angle):
        self.rotate_right(-angle)

    def rotate_right(self, angle):
        r = angle % 360 // 90
        assert(isinstance(r, int))
        self._dir = self._dirs[(self._dirs.index(self._dir) + r) % len(self._dirs)]

    def get_manhattan_dist(self):
        return abs(self._ns) + abs(self._ew)


def parse_ins(line):
    r = re.search(r'^([A-Z])(\d+)$', line)
    return r.group(1), int(r.group(2))


def interpret_ins(ins, ship):
    dirr, steps = ins
    if dirr in ['N', 'S', 'E', 'W']:
        ship.sail_in_direction(dirr, steps)
    elif dirr == 'F':
        ship.sail_forward(steps)
    elif dirr == 'L':
        ship.rotate_left(steps)
    elif dirr == 'R':
        ship.rotate_right(steps)
    else:
        raise AssertionError(f'Unknown instruction: {ins}')


if __name__ == '__main__':
    with open('input1', 'r') as file:
        route = [parse_ins(i) for i in file.readlines()]
    s = Ship('E')
    [interpret_ins(i, s) for i in route]
    print(s.get_manhattan_dist())
