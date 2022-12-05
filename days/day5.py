from copy import deepcopy
from math import ceil

from utils.aoc_utils import AOCDay, day


@day(5)
class Day5(AOCDay):
    def common(self):
        strPlan, strInstructions = self.rawData.split('\n\n')
        plan = strPlan.split('\n')

        # Parsing stacks
        plan.reverse()
        numStacks = ceil(len(plan[0])/4)
        self.stacks = [[] for _ in range(numStacks)]

        for line in plan[1:]:
            for i in range(numStacks):
                if line[1 + i * 4] != ' ':
                    self.stacks[i].append(line[1 + i * 4])

        # Parsing instructions
        self.instructions = []
        for line in strInstructions.split('\n'):
            _, n, _, fromm, _, to = line.split(' ')
            self.instructions.append((int(n), int(fromm)-1, int(to)-1))

    def part1(self):
        stacksP1 = deepcopy(self.stacks)

        for instruction in self.instructions:
            self.executeInstruction(stacksP1, instruction)

        return self.peekAllStacks(stacksP1)

    def part2(self):
        stacksP2 = deepcopy(self.stacks)

        for instruction in self.instructions:
            self.executeInstructionPart2(stacksP2, instruction)

        return self.peekAllStacks(stacksP2)

    def peekAllStacks(self, stacks):
        return ''.join([stacks[i][-1] if len(stacks[i]) > 0 else '' for i in range(len(stacks))])

    def executeInstruction(self, stacks, instruction):
        for _ in range(instruction[0]):
            stacks[instruction[2]].append(
                stacks[instruction[1]].pop())

    def executeInstructionPart2(self, stacks, instruction):
        popped = [stacks[instruction[1]].pop()
                  for _ in range(instruction[0])]

        popped.reverse()
        for crate in popped:
            stacks[instruction[2]].append(crate)
