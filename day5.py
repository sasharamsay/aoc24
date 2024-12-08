# --- Day 5: Print Queue ---
# https://adventofcode.com/2024/day/5

import math

rules = []
updates = []


def read(filename):
    rules.clear()
    updates.clear()

    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if line == '\n':
                break
            rules.append(list(int(x) for x in line.strip('\n').split('|')))
        while True:
            line = file.readline()
            if len(line) == 0:
                break
            updates.append(list(int(x) for x in line.strip('\n').split(',')))


def apply_rule(update, rule):
    result = update
    result.remove(rule[0])
    result.insert(result.index(rule[1]), rule[0])
    return result


def day_5(filename):
    read(filename)
    correct_middle_sum = 0

    for update in updates:
        correct = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    correct = False
        if correct:
            correct_middle_sum += update[math.floor(len(update) / 2)]

    return correct_middle_sum


def day_5_part_2(filename):
    read(filename)
    updates_to_reorder = []
    reordered_middle_sum = 0

    for update in updates:
        repeat = True
        add = False
        while repeat:  # apply rules until all are valid (fixed point algorithm)
            repeat = False
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        add = True
                        repeat = True
                        update = apply_rule(update, rule)
        if add:
            updates_to_reorder.append(update)

    for update in updates_to_reorder:
        reordered_middle_sum += update[math.floor(len(update) / 2)]

    return reordered_middle_sum
