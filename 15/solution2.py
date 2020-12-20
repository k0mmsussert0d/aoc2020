def solve(input, target):
    numbers = {n: idx + 1 for idx, n in enumerate(input[:-1])}
    prev = input[-1]
    for i in range(len(input), target+1):
        prev = input[i-1]
        if n := numbers.get(prev):
            input.append(i - n)
        else:
            input.append(0)
        numbers[prev] = i

    return prev


if __name__ == '__main__':
    with open('./input1', 'r') as file:
        input = [int(i) for i in file.readline().split(',')]

    print(solve(input, 30_000_000))
