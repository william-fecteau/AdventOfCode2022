from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        self.elveSums = [sum(map(int, calorie.split()))
                         for calorie in self.rawData.split('\n\n')]

    def part1(self):
        return max(self.elveSums)

    def part2(self):
        return sum(sorted(self.elveSums, reverse=True)[:3])
