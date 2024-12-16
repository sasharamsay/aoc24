# --- Day 7: Bridge Repair ---
# https://adventofcode.com/2024/day/7

targets = []
operand_list = []


def unconcatenate(target, operand):
    target_str = str(target)
    remove_str = str(operand)
    len_remove_str = len(remove_str)
    return int(target_str[:-len_remove_str])


def solve(target, operands, concat):  # changing approach to work backwards
    if len(operands) == 1:
        return operands[0] == target
    elif target - operands[-1] < 0 or len(operands) > target:
        return False
    else:
        x = 10 ** len(str(operands[-1]))
        if target % operands[-1] == 0 and solve(int(target / operands[-1]), operands[:-1], concat):
            return True
        if target % x == operands[-1] and concat and solve(unconcatenate(target, operands[-1]), operands[:-1], True):
            return True
        return solve(target - operands[-1], operands[:-1], concat)


def read(filename):
    targets.clear()
    operand_list.clear()

    for line in open(filename, 'r').readlines():
        targets.append(int(line.split(':')[0]))
        operand_list.append(list(int(x) for x in line.split(':')[1].removeprefix(' ').split(' ')))


def day_7(filename):
    read(filename)
    possible_sum = 0

    for i, target in enumerate(targets):
        print(str(operand_list[i]))
        if solve(target, operand_list[i], False):
            possible_sum += target

    print(possible_sum)
    return possible_sum


def day_7_part_2(filename):
    read(filename)
    possible_sum_normal = 0
    possible_sum_extra = 0

    for i, target in enumerate(targets):
        if solve(target, operand_list[i], False):
            possible_sum_normal += target
        elif solve(target, operand_list[i], True):
            possible_sum_extra += target
    return possible_sum_normal + possible_sum_extra