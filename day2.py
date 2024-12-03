# --- Day 2: Red-Nosed Reports ---
# https://adventofcode.com/2024/day/2

reports = []


class Report:
    def __init__(self, int_input):
        self.levels = int_input

        self.sub_levels = []
        for i in range(len(self.levels)):
            new_level = self.levels.copy()
            new_level.pop(i)
            self.sub_levels.append(new_level)

        self.diff = [self.levels[i] - self.levels[i - 1] for i in range(1, len(self.levels))]
        self.safe = self.determine_safety()
        self.dampened_safe = self.determine_dampened_safety()

    def determine_safety(self):
        safe = True
        signed = False

        for i in range(len(self.diff)):
            safe = True
            if i == 0:
                signed = self.diff[i] < 0
            else:
                if (self.diff[i] < 0) != signed:
                    safe = False
                    break
            if self.diff[i] > 3 or self.diff[i] < -3 or self.diff[i] == 0:
                safe = False
                break

        return safe

    def determine_dampened_safety(self):
        safe = False
        for sub_level in self.sub_levels:
            report = Report(sub_level)
            if report.determine_safety():
                return True
        return safe


def read(filename):
    reports.clear()
    for line in open(filename, 'r').readlines():
        line_ints = [int(num) for num in line.split()]
        reports.append(Report(line_ints))


def day_2(filename):
    read(filename)
    num_safe = 0

    for report in reports:
        if report.safe:
            num_safe += 1

    return num_safe


def day_2_part_2(filename):
    read(filename)
    num_safe = 0

    for report in reports:
        if report.dampened_safe:
            num_safe += 1

    return num_safe
