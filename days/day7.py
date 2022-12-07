from utils.aoc_utils import AOCDay, day


class Node:
    def __init__(self, name, size, isDir, parent):
        self.name = name
        self.children = []
        self.isDir = isDir
        self.parent = parent
        self.size = size

    def getChildByName(self, name: str):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def __str__(self):
        type = "file" if not self.isDir else "dir"
        return f"- {self.name} ({type}, size={self.size})"


class Tree:
    def __init__(self):
        self.root = Node("/", 0, True, None)
        self.allDirs = []

    def addChild(self, parent: Node, child: Node):
        parent.children.append(child)

    def computeSizeRec(self, node: Node):
        if node.isDir:
            for child in node.children:
                if child.isDir:
                    self.computeSizeRec(child)

            node.size = sum(map(lambda x: x.size, node.children))
            self.allDirs.append(node)

    def print(self):
        print(self.root)
        self.printRec(self.root, 1)

    def printRec(self, node, depth):
        indent = "\t" * depth
        for child in node.children:
            print(f"{indent}{child}")
            self.printRec(child, depth+1)


@day(7)
class Day7(AOCDay):
    def common(self):
        # Parsing commands
        self.commands = []
        cmdOutput = cmd = arg = None
        for line in self.inputData:
            if line.startswith("$"):
                if cmd is not None:
                    self.commands.append((cmd, arg, cmdOutput))
                cmdOutput = []
                splitted = line[2:].split(" ")
                cmd = splitted[0]
                arg = splitted[1] if len(splitted) > 1 else None
            else:
                cmdOutput.append(line)

        if cmd is not None:
            self.commands.append((cmd, arg, cmdOutput))

        # Building the tree
        self.tree = Tree()
        cwd = None
        for cmd, arg, output in self.commands:
            if cmd == "cd":
                cwd = self.cd(cwd, arg)
            elif cmd == "ls":
                self.ls(cwd, output)
        self.tree.computeSizeRec(self.tree.root)

    def part1(self):
        # print(self.tree.print())
        return sum([dir.size for dir in self.tree.allDirs if dir.size <= 100000])

    def part2(self):
        spaceToFree = 30000000 - (70000000 - self.tree.root.size)
        self.tree.allDirs.sort(key=lambda x: x.size)
        for dir in self.tree.allDirs:
            if dir.size > spaceToFree:
                return dir.size
        return -1

    def cd(self, cwd: Node, input: str):
        if input == "/":
            return self.tree.root
        elif input == "..":
            return cwd.parent

        newCwd = cwd.getChildByName(input)
        if newCwd is not None and not newCwd.isDir:
            return None

        return newCwd

    def ls(self, cwd: Node, output: list[str]):
        for line in output:
            left, name = line.split(" ")
            if left == "dir":
                node = Node(name, 0, True, cwd)
            else:
                node = Node(name, int(left), False, cwd)

            self.tree.addChild(cwd, node)
