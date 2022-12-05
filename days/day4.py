from utils.aoc_utils import AOCDay, day


@day(4)
class Day4(AOCDay):
    def common(self):
        self.pairs = []
        for line in self.inputData:
            self.pairs.append([[tuple(map(int, r1.split(
                '-'))), tuple(map(int, r2.split('-')))] for (r1, r2) in [line.split(',')]][0])

    def isFullyContained(self, a, b, c, d):
        return (a <= c and b >= d) or (c <= a and d >= b)

    def isOverlapping(self, a, b, c, d):
        return (a <= c and b >= c) or (c <= a and d >= a)

    def part1(self, t):
        return sum(map(lambda x: self.isFullyContained(*x[0], *x[1]), self.pairs))

    def part2(self):
        return sum(map(lambda x: self.isOverlapping(*x[0], *x[1]), self.pairs))
