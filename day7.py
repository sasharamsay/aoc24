# --- Day 7: Bridge Repair ---
# https://adventofcode.com/2024/day/7

targets = []
operands_all = []


def solve(target, operands, concat):  # changing approach to work backwards
    if len(operands) == 1:
        return operands[0] == target
    elif target - operands[-1] < 0 or len(operands) > target:
        return False
    else:
        if target % operands[-1] == 0 and solve(int(target / operands[-1]), operands[:-1], concat):
            return True
        if (concat and target % 10 ** len(str(operands[-1])) == operands[-1]
                and solve(int(str(target)[:-len(str(operands[-1]))]), operands[:-1], True)):
            return True
        return solve(target - operands[-1], operands[:-1], concat)


def read(filename):
    targets.clear()
    operands_all.clear()
    for line in open(filename, 'r').readlines():
        targets.append(int(line.split(':')[0]))
        operands_all.append(list(int(x) for x in line.split(':')[1].removeprefix(' ').split(' ')))


def day_7(filename):
    read(filename)
    possible_sum = 0

    for target, operands in zip(targets, operands_all):
        if solve(target, operands, False):
            possible_sum += target
    return possible_sum


def day_7_part_2(filename):
    read(filename)
    possible_sum = 0
    possible_sum_concat = 0

    for target, operands in zip(targets, operands_all):
        if solve(target, operands, False):
            possible_sum += target
        elif solve(target, operands, True):
            possible_sum_concat += target
    return possible_sum + possible_sum_concat
