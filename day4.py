# --- Day 4: Ceres Search ---
# https://adventofcode.com/2024/day/4

search = []


def next_letter_found(start, direction, letter):
    row = start[0]
    col = start[1]

    if 'north' in direction:
        row = row - 1
    if 'south' in direction:
        row = row + 1
    if 'east' in direction:
        col = col - 1
    if 'west' in direction:
        col = col + 1
    if row > len(search) - 1 or col > len(search[0]) - 1 or row < 0 or col < 0 or search[row][col] != letter:
        return -1, -1

    return row, col


def directions_match(s, m): # same letters can't be opposite of each other
    s_match = False
    m_match = False
    for direction in ('north', 'south', 'east', 'west'):
        if direction in s[0] and direction in s[1]:
            s_match = True
        if direction in m[0] and direction in m[1]:
            m_match = True
    return s_match and m_match


def read(filename):
    search.clear()
    for line in open(filename, 'r').readlines():
        line_arr = []
        for char in line:
            if char != '\n':
                line_arr.append(char)
        search.append(line_arr)


def day_4(filename):
    read(filename)
    directions = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest']
    num_xmas = 0
    x_pos = []

    for i, row in enumerate(search):
        for j, col in enumerate(row):
            if col == 'X':
                x_pos.append((i, j))

    for x in x_pos:
        for direction in directions:
            pos_found = x
            for letter in ('M', 'A', 'S'):
                pos_found = next_letter_found(pos_found, direction, letter)
                if pos_found == (-1, -1):
                    break
            if pos_found != (-1, -1):
                num_xmas += 1

    return num_xmas


def day_4_part_2(filename):
    directions = ['northeast', 'southeast', 'southwest', 'northwest']

    read(filename)
    num_xmas = 0
    a_pos = []

    for i, row in enumerate(search):
        for j, col in enumerate(row):
            if col == 'A':
                a_pos.append((i, j))

    for a in a_pos:
        s_count = 0
        s_directions = []
        m_count = 0
        m_directions = []
        for direction in directions:
            if next_letter_found(a, direction, 'S') != (-1, -1):
                s_count += 1
                s_directions.append(direction)
            if next_letter_found(a, direction, 'M') != (-1, -1):
                m_count += 1
                m_directions.append(direction)
        if s_count == 2 and m_count == 2 and directions_match(s_directions, m_directions):
            num_xmas += 1

    return num_xmas
