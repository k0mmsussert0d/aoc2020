if __name__ == '__main__':
    with open('input1', 'r') as file:
        start = int(file.readline().strip())
        departs = [int(i) for i in file.readline().split(',') if i.isdigit()]
    waiting_times = [i - start % i for i in departs]
    wait = min(waiting_times)
    your_bus = departs[waiting_times.index(wait)]
    print(your_bus*wait)
