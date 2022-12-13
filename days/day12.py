from utils.aoc_utils import AOCDay, day

INFINITY = float('inf')


class Graph:
    def __init__(self, adjList):
        self.adjList = adjList
        self.nbNodes = len(adjList)

    def getNeighbours(self, node):
        return self.adjList[node]

    def getDistance(self, node1, node2):
        return 1  # Always one hihi

    def getShortestPath(self, start, end):
        distances = [INFINITY] * self.nbNodes
        distances[start] = 0
        previous = [None] * self.nbNodes

        queue = [start]
        while queue:
            node = queue.pop(0)

            for neighbour in self.getNeighbours(node):
                distance = distances[node] + self.getDistance(node, neighbour)
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    previous[neighbour] = node
                    queue.append(neighbour)

        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous[node]

        return path[::-1]


@day(12)
class Day12(AOCDay):
    def common(self):
        self.heightMap = [[ord(c) for c in line] for line in self.inputData]
        self.nbRows = len(self.heightMap)
        self.nbCols = len(self.heightMap[0])
        self.nbNodes = self.nbRows * self.nbCols
        self.adjencencyList = []

        for i in range(self.nbRows):
            for j in range(self.nbCols):
                if self.heightMap[i][j] == ord('S'):
                    self.startPos = (i, j)
                    self.heightMap[i][j] = ord('a')
                elif self.heightMap[i][j] == ord('E'):
                    self.endPos = (i, j)
                    self.heightMap[i][j] = ord('z')

        for i in range(self.nbRows):
            for j in range(self.nbCols):
                curNodeNeighbours = []
                for neighbourPos in self.getNeighbours((i, j)):
                    depthDiff = self.heightMap[neighbourPos[0]
                                               ][neighbourPos[1]] - self.heightMap[i][j]
                    if depthDiff <= 0 or depthDiff == 1:
                        destNode = self.posToNodeNum(neighbourPos)
                        curNodeNeighbours.append(destNode)

                self.adjencencyList.append(curNodeNeighbours)

        # for i, l in enumerate(self.adjencencyList):
        #     print(f"{i} = {list(map(self.nodeToPos, l))}", sep=',')

        self.graph = Graph(self.adjencencyList)

    def posToNodeNum(self, pos):
        return pos[0] * self.nbCols + pos[1]

    def nodeToPos(self, node):
        return (node // self.nbCols, node % self.nbCols)

    def getNeighbours(self, pos):
        i, j = pos
        neighbours = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        return [n for n in neighbours
                if n[0] >= 0 and n[0] < self.nbRows and n[1] >= 0 and n[1] < self.nbCols]

    def printPath(self, path):
        for i in range(self.nbRows):
            for j in range(self.nbCols):
                t = self.posToNodeNum((i, j))
                if t in path:
                    print("P", end='')
                else:
                    print(".", end='')
            print()

    def part1(self):
        shortestPath = self.graph.getShortestPath(
            self.posToNodeNum(self.startPos), self.posToNodeNum(self.endPos))
        self.printPath(shortestPath)
        return len(shortestPath) - 1

    def part2(self):
        return 0
