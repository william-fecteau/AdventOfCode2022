import itertools

from utils.aoc_utils import AOCDay, day


@day(15)
class Day15(AOCDay):
    def common(self):
        self.sensors = []
        self.beacons = []
        self.dists = []
        for line in self.inputData:
            left, right = line.split(":")
            sensorX = int(left[left.find("x") + 2:left.find(",")])
            sensorY = int(left[left.find("y") + 2:])
            beaconX = int(right[right.find("x") + 2:right.find(",")])
            beaconY = int(right[right.find("y") + 2:])
            dist = abs(sensorX - beaconX) + abs(sensorY - beaconY)

            self.sensors.append((sensorX, sensorY))
            self.beacons.append((beaconX, beaconY))
            self.dists.append(dist)

    def compute(self, minRow, maxRow, part1):
        for row in range(minRow, maxRow):
            overlaps = []

            for (sensorX, sensorY), dist in zip(self.sensors, self.dists):
                distFromRow = abs(sensorY - row)

                # Only continue with rows close enough from the row of interest
                if distFromRow > dist:
                    continue

                overlaps.append((sensorX - dist + distFromRow,
                                sensorX + dist - distFromRow + 1))

            if part1:
                beaconsOfRow = len(
                    {beaconX for (beaconX, beaconY) in self.beacons if beaconY == row})
                minX, maxX = zip(*overlaps)
                return max(maxX) - min(minX) - beaconsOfRow

            overlaps = sorted(overlaps)
            cur = 0
            for (start1, stop1), (start2, stop2) in itertools.pairwise(overlaps):
                if start2 > cur and start2 > stop1:
                    return (stop1 * 4_000_000 + row)
                else:
                    cur = max(stop1, cur)

    def part1(self):
        return self.compute(2_000_000, 2_000_001, True)

    def part2(self):
        return self.compute(0, 4_000_001, False)
