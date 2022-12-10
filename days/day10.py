import numpy as np

from utils.aoc_utils import AOCDay, day


@day(10)
class Day10(AOCDay):
    def common(self):
        toAdd = None
        x = 1
        cycle = i = 0
        self.cycleValues = []
        while cycle <= 240 and i < len(self.inputData):
            cycle += 1
            line = self.inputData[i]

            self.cycleValues.append(x)
            if toAdd is not None:
                x += toAdd
                toAdd = None
                i += 1
            elif line.startswith("addx"):
                _, value = line.split(' ')
                toAdd = int(value)
            elif line.startswith("noop"):
                i += 1

    def part1(self):
        return sum([self.cycleValues[i-1] * i for i in [20, 60, 100, 140, 180, 220]])

    def part2(self):
        screen = "\n"
        for i, x in enumerate(self.cycleValues):
            drawingPos = i % 40

            if i != 0 and i % 40 == 0:
                screen += "\n"

            if drawingPos in [x-1, x, x+1]:
                screen += "#"
            else:
                screen += "."

        return screen
