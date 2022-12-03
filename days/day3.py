from utils.aoc_utils import AOCDay, day


@day(3)
class Day3(AOCDay):
    def common(self):
        pass

    def part1(self):
        return sum(map(lambda line: self.findDuplicates(line[:len(line)//2], line[len(line)//2:])[0], self.inputData))

    def part2(self):
        points = 0

        for i in range(0, len(self.inputData), 3):
            d1 = set(self.findDuplicates(
                self.inputData[i], self.inputData[i+1]))
            d2 = set(self.findDuplicates(
                self.inputData[i], self.inputData[i+2]))
            d3 = set(self.findDuplicates(
                self.inputData[i+1], self.inputData[i+2]))

            points += list(d1.intersection(d2, d3))[0]

        return points

    def getPointsOfChar(self, char):
        return ord(char) - 96 if char.islower() else ord(char) - 38

    def findDuplicates(self, part1, part2):
        return list(map(self.getPointsOfChar, set(part1).intersection(set(part2))))
