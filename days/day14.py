import numpy as np

from utils.aoc_utils import AOCDay, day

AIR = 0
ROCK = 1
SAND = 2


@day(14)
class Day14(AOCDay):
    def common(self):
        lines = []
        for strLine in self.inputData:
            line = [(int(x), int(y)) for (x, y) in [strPoint.split(',')
                                                    for strPoint in strLine.split(' -> ')]]
            lines.append(line)

        allPoints = sum(lines, [])
        maxX = max(map(lambda point: point[0], allPoints))
        maxY = max(map(lambda point: point[1], allPoints))

        # Building the map
        # Let some x space for sand to make a pyramid
        self.map = np.zeros((maxY + 3, maxX + 200))
        self.sandStartPos = (500, 0)
        self.sandCounter = 0
        for line in lines:
            for i in range(len(line)-1):
                x1, y1 = line[i]
                x2, y2 = line[i + 1]

                if (x2 < x1):
                    x1, x2 = x2, x1
                if (y2 < y1):
                    y1, y2 = y2, y1

                self.map[y1:y2+1, x1:x2+1] = ROCK

    def isCellFree(self, pos):
        x, y = pos

        # Out of bounds
        if x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map):
            return False

        return self.map[y, x] == AIR

    def simulate(self, isPart2):
        canPlaceSand = True
        while canPlaceSand:
            self.sandPos = self.sandStartPos

            canSandMove = True
            while canSandMove:
                x, y = self.sandPos

                if not isPart2 and y == len(self.map) - 1:
                    canPlaceSand = False
                    break

                nextPos = self.sandPos
                for pos in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
                    if self.isCellFree(pos):
                        self.sandPos = pos
                        break

                if self.sandPos == nextPos:
                    canSandMove = False
                    self.sandCounter += 1
                    self.map[self.sandPos[1], self.sandPos[0]] = SAND

                    if self.sandPos == self.sandStartPos:
                        canPlaceSand = False
                        break

        return self.sandCounter

    def part1(self):
        return self.simulate(False)

    def part2(self):
        # Floor
        self.map[len(self.map) - 1, :] = ROCK

        return self.simulate(True)
