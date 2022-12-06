total = 0

from string import ascii_lowercase, ascii_uppercase

def get_priority(letter):
    all_letters = ascii_lowercase +  ascii_uppercase
    return all_letters.index(letter) + 1

def part1():
    with open("day3.txt") as f:
        for line in f:
            line = line.strip()
            h1 = line[0:len(line)//2]
            h2 = line[len(line)//2:]

            for letter in h1: 
                if letter in h2:
                    print(get_priority(letter))
                    total += get_priority(letter)
                    break

    print(total)

def part2():
    total = 0
    sacks = []
    with open("day3.txt") as f:
        for line in f:
            sack = line.strip()
            sacks.append(sack)

    for i in range(0, len(sacks), 3):
        for letter in sacks[i]:
            if letter in sacks[i + 1] and letter in sacks[i + 2]:
                total += get_priority(letter)
                break

    print(total)

part2()