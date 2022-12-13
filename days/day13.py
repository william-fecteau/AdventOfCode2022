import functools

from utils.aoc_utils import AOCDay, day


# > 0 if left is before right
# = 0 if left is equal to right
# < 0 if left is after right
def compareInts(left, right):
    if left == right:
        return 0

    return 1 if left < right else -1


# > 0 if left is before right
# = 0 if left is equal to right
# < 0 if left is after right
def compare(left, right):
    # Base case
    if isinstance(left, int) and isinstance(right, int):
        return compareInts(left, right)

    # Past this point we only compare lists
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    for i in range(max(len(left), len(right))):
        if i >= len(left):
            return 1
        elif i >= len(right):
            return -1
        result = compare(left[i], right[i])
        if result != 0:
            return result

    return 0


@day(13)
class Day13(AOCDay):
    def common(self):
        self.pairedPackets = [(eval(left), eval(right)) for (left, right) in [pairs.split('\n')
                                                                              for pairs in self.rawData.split('\n\n')]]

    def part1(self):
        valids = []
        for pairs in self.pairedPackets:
            left, right = pairs
            result = compare(left, right)
            valids.append(result)

        return sum([i+1 for i in range(len(valids)) if valids[i] == 1])

    def part2(self):
        packets = []
        for packetPair in self.pairedPackets:
            packets.extend(packetPair)

        # Adding extra packets
        START = [[2]]
        END = [[6]]
        packets.append(START)
        packets.append(END)

        packets.sort(key=functools.cmp_to_key(compare), reverse=True)

        return (packets.index(START) + 1) * (packets.index(END) + 1)
