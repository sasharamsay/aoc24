# --- Day 1: Historian Hysteria ---
# https://adventofcode.com/2024/day/1

list_1, list_2 = [], []


def read(filename):
    list_1.clear()
    list_2.clear()
    for line in open(filename, 'r').readlines():
        pair = line.split()
        list_1.append(int(pair[0]))
        list_2.append(int(pair[1]))


def day_1(filename):
    distance_sum = 0
    read(filename)
    list_1.sort()
    list_2.sort()

    for i in range(min(len(list_1), len(list_2))):
        distance_sum += abs(list_1[i] - list_2[i])

    return distance_sum


def day_1_part_2(filename):
    similarity_score = 0
    read(filename)

    for num in list_1:
        similarity_score += num * list_2.count(num)

    return similarity_score
