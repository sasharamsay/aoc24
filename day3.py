# --- Day 3: Mull It Over ---
# https://adventofcode.com/2024/day/3

import re


def read(filename):
    with open(filename, 'r') as file:
        return file.read()


def day_3(filename):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    content = read(filename)
    product_sum = 0
    matches = re.findall(pattern, content)

    for match in matches:
        product_sum += int(match[0]) * int(match[1])

    return product_sum


def day_3_part_2(filename):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|(?:don't\(\))|(?:do\(\))"

    content = read(filename)
    product_sum = 0
    matches = re.findall(pattern, content)
    do = True

    for match in matches:
        print(match)
        if do and match.startswith("mul"):
            start = match.find("(") + 1
            end = match.find(")")
            innards = match[start:end]
            product_sum += int(innards.split(",")[0]) * int(innards.split(",")[1])
        elif match.startswith("do("):
            do = True
        elif match.startswith("don't"):
            do = False

    return product_sum

