from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        self.elves = []
        self.currentElve = []
        for line in self.inputData:
            if (line == ""):
                self.elves.append(self.currentElve)
                self.currentElve = []
                continue

            self.currentElve.append(int(line))

        self.elveSums = list(map(lambda x: sum(x), self.elves))
        return 0

    def part1(self):
        return max(self.elveSums)

    def part2(self):
        return sum(sorted(self.elveSums, reverse=True)[:3])
