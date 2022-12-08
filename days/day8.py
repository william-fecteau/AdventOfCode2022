import numpy as np

from utils.aoc_utils import AOCDay, day


@day(8)
class Day8(AOCDay):
    def common(self):
        self.trees = np.array([[int(c) for c in line]
                              for line in self.inputData])

    def part1(self):
        treeCount = sum([self.isTreeVisible(i, j)[0] for i in range(
            1, len(self.trees) - 1) for j in range(1, len(self.trees) - 1)])

        # To account for the edges that we don't check
        return treeCount + 2 * len(self.trees) + 2 * len(self.trees) - 4

    def part2(self):
        return max([self.isTreeVisible(i, j)[1] for i in range(
            1, len(self.trees) - 1) for j in range(1, len(self.trees) - 1)])

    # Check if the tree is visible and return the scenic score
    def isTreeVisible(self, i, j):
        tree = self.trees[i, j]

        row = self.trees[i, :]
        col = self.trees[:, j]

        toCheck = [row[j-1::-1], row[j+1:len(self.trees)],
                   col[i-1::-1], col[i+1:len(self.trees):]]

        shouldReturnVisible = False
        totalScenicScore = 1
        for line in toCheck:
            scenicScore = 0
            isVisible = True
            for height in line:
                scenicScore += 1
                if height >= tree:
                    isVisible = False
                    break

            totalScenicScore *= scenicScore
            if isVisible:
                shouldReturnVisible = True

        return (shouldReturnVisible, totalScenicScore)
