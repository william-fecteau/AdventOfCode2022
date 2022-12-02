from utils.aoc_utils import AOCDay, day


@day(2)
class Day2(AOCDay):
    def common(self):
        self.winAgainst = {
            "A": "C",
            "B": "A",
            "C": "B"
        }

        self.loseAgainst = {
            "C": "A",
            "A": "B",
            "B": "C"
        }

    def part1(self):
        return sum(map(lambda x: self.play(x.replace("X", "A").replace(
            "Y", "B").replace("Z", "C")), self.inputData))

    def part2(self):
        return sum(map(lambda x: self.play(self.decideWhatToPlay(x)), self.inputData))

    def play(self, input):
        POINTS = {
            "A": 1,
            "B": 2,
            "C": 3
        }

        opponent, you = input.split(" ")

        # Shape point
        points = POINTS[you]

        # Draw
        if you == opponent:
            return points + 3

        # You win
        if self.winAgainst[you] == opponent:
            return points + 6

        # Opponent wins
        return points

    def decideWhatToPlay(self, input):
        opponent, strategy = input.split(" ")

        if strategy == "X":
            return f"{opponent} {self.winAgainst[opponent]}"
        elif strategy == "Z":
            return f"{opponent} {self.loseAgainst[opponent]}"

        return f"{opponent} {opponent}"
