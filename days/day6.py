from utils.aoc_utils import AOCDay, day


@day(6)
class Day6(AOCDay):
    def common(self):
        pass

    def part1(self):
        return self.getPosition(4)

    def part2(self):
        return self.getPosition(14)

    def getPosition(self, nbConsecutiveDiffChar):
        groups = map(set, [self.rawData[i-nbConsecutiveDiffChar:i]
                           for i in range(nbConsecutiveDiffChar, len(self.rawData))])
        for i, group in enumerate(groups):
            if len(group) == nbConsecutiveDiffChar:
                return i+nbConsecutiveDiffChar
        return -1
