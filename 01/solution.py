if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()

    lines = [int(i) for i in lines]

    for i in lines:
        for j in lines:
            if i == j:
                continue
            else:
                for k in lines:
                    if k == i or k == j:
                        continue
                    else:
                        if i + j + k == 2020:
                            print(i, j, k, i*j*k)
