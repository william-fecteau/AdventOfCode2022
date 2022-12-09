import numpy as np

from utils.aoc_utils import AOCDay, day


@day(9)
class Day9(AOCDay):
    def common(self):
        pass

    def part1(self):
        self.allKnots = [(0, 0)] * 2
        allTailPos = set()
        for strMove in self.inputData:
            letter, num = strMove.split(" ")
            for _ in range(int(num)):
                self.move(letter)
                allTailPos.add(self.allKnots[-1])

        return len(allTailPos)

    def printAllKnots(self):
        print("-----------------")
        cols = 30
        rows = 30
        matrix = [['.' for _ in range(cols)] for _ in range(rows)]
        for i, knot in enumerate(self.allKnots):
            matrix[knot[0] + 10][knot[1] + 10] = str(i)

        for i in range(rows-1, -1, -1):
            for j in range(cols):
                print(matrix[i][j], end=' ')
            print()

    def part2(self):
        self.allKnots = [(0, 0)] * 10
        allTailPos = set()
        for strMove in self.inputData:
            letter, num = strMove.split(" ")
            # print(f"================={strMove}====================")
            for _ in range(int(num)):
                self.move(letter)
                allTailPos.add(self.allKnots[-1])
                # self.printAllKnots()

        return len(allTailPos)

    def areNeighbours(self, knotPosA, knotPosB):
        for move in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            if (knotPosA[0] + move[0], knotPosA[1] + move[1]) == knotPosB:
                return True
        return False

    def addTuples(self, tupleA, tupleB):
        return (tupleA[0] + tupleB[0], tupleA[1] + tupleB[1])

    def move(self, move):
        moveTuple = self.getMoveTuple(move)

        # Moving the head
        self.allKnots[0] = self.addTuples(self.allKnots[0], moveTuple)

        for i in range(len(self.allKnots) - 1):
            curHead = self.allKnots[i]
            curTail = self.allKnots[i + 1]

            tailMove = (0, 0)
            if not self.areNeighbours(curHead, curTail):
                dRow = curHead[0] - curTail[0]
                dCol = curHead[1] - curTail[1]

                dRow = dRow // abs(dRow) if dRow != 0 else 0
                dCol = dCol // abs(dCol) if dCol != 0 else 0

                tailMove = (dRow, dCol)

            curTail = self.addTuples(curTail, tailMove)

            self.allKnots[i] = curHead
            self.allKnots[i + 1] = curTail

    def getMoveTuple(self, move):
        if move == "U":
            return (1, 0)
        elif move == "D":
            return (-1, 0)
        elif move == "R":
            return (0, 1)
        elif move == "L":
            return (0, -1)
        raise Exception("Invalid move")
