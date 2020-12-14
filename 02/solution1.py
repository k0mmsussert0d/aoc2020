from collections import Counter
import re


def is_valid(letter, word, min, max):
    return min <= Counter(word).get(letter, 0) <= max


if __name__ == '__main__':
    passwords = []
    pattern = re.compile('^(\d+)-(\d+) (\w): ([a-z]+)$')
    with open('input1', 'r') as file:
        while line := file.readline():
            passwords.append(pattern.findall(line)[0])
    print(sum([is_valid(n[2], n[3], int(n[0]), int(n[1])) for n in passwords]))
