import math
from copy import deepcopy

from utils.aoc_utils import AOCDay, day


@day(11)
class Day11(AOCDay):
    def common(self):
        self.monkeys = []
        for monkeyDef in self.rawData.split("\n\n"):
            lines = monkeyDef.split("\n")
            monkey = {
                "startingItems": [int(num) for num in lines[1][18:].split(", ")],
                "operation": lines[2][19:].replace(" ", ""),
                "test": int(lines[3][21:]),
                "actionIfTrue": int(lines[4][29:]),
                "actionIfFalse": int(lines[5][30:]),
                "businessCounter": 0
            }
            self.monkeys.append(monkey)

    def playRound(self, monkeys, isPart1):
        common = math.prod(monkey["test"] for monkey in monkeys)

        for monkey in monkeys:
            for worryLvl in monkey["startingItems"]:
                operation = monkey["operation"].replace("old", str(worryLvl))

                # Compute worry level depending on part
                if isPart1:
                    newWorryLvl = int(eval(operation) / 3)
                else:
                    newWorryLvl = int(eval(operation)) % common

                monkeyToThrow = monkey["actionIfTrue"] if newWorryLvl % monkey["test"] == 0 else monkey["actionIfFalse"]
                monkeys[monkeyToThrow]["startingItems"].append(newWorryLvl)
                monkey["businessCounter"] += 1

            monkey["startingItems"].clear()

    def part1(self):
        part1Monkeys = deepcopy(self.monkeys)
        for _ in range(20):
            self.playRound(part1Monkeys, True)

        return math.prod(sorted([monkey["businessCounter"] for monkey in part1Monkeys], reverse=True)[0:2])

    def part2(self):
        part2Monkeys = deepcopy(self.monkeys)
        for _ in range(10_000):
            self.playRound(part2Monkeys, False)

        return math.prod(sorted([monkey["businessCounter"] for monkey in part2Monkeys], reverse=True)[0:2])
