def rindex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1


if __name__ == '__main__':
    with open('./input1', 'r') as file:
        num = [int(i) for i in file.readline().split(',')]

    for i in range(len(num), 2021):
        x = 0
        if num.count(num[i-1]) > 1:
            x = i - rindex(num[:i-1], num[i-1]) - 1
        num.append(x)
    print(num[2019])
