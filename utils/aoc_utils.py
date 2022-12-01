import os
import sys
import time

import requests


def day(dayNumber):
    def day_decorator(cls):
        AOCDays.getInstance().addDay(dayNumber, cls)
        return cls
    return day_decorator


class AOCDay:
    year = 2020
    dayNumber = 0
    inputFilename = ""
    outputFilename = ""
    sessionToken = ""
    inputData = None

    def __init__(self, year, dayNumber, sessionToken):
        self.year = int(year)
        self.dayNumber = int(dayNumber)
        self.sessionToken = sessionToken

        fileName = "day" + str(dayNumber) + ".txt"

        # Configuring inputs
        self.inputPath = os.getcwd() + "/inputs"
        if not os.path.exists(self.inputPath):
            os.makedirs(self.inputPath)
        self.inputPath += "/" + fileName

        # Configuring outputs
        self.outputPath = os.getcwd() + "/outputs"
        if not os.path.exists(self.outputPath):
            os.makedirs(self.outputPath)
        self.outputPath += "/" + fileName

    def run(self):
        # Getting input
        self.downloadInput()

        # Common thinggy
        startTime = time.time()
        self.common()
        time0 = time.time() - startTime

        # Part 1
        startTime = time.time()
        answer1 = self.part1()
        time1 = time.time() - startTime

        # Part 2
        startTime = time.time()
        answer2 = self.part2()
        time2 = time.time() - startTime

        totalTime = time0 + time1 + time2

        # Writing output
        self.writeOutput(
            "====================== Day" +
            str(self.dayNumber) + " ======================",
            "Common time (ms) : " + str(time0),
            "---------------------------------------------------",
            "Part 1 : " + str(answer1),
            "Time (ms): " + str(time1),
            "---------------------------------------------------",
            "Part 2 : " + str(answer2),
            "Time (ms): " + str(time2),
            "---------------------------------------------------",
            "Total time (ms): " + str(totalTime)
        )

    def downloadInput(self):
        # If file already exists, only read it
        if os.path.exists(self.inputPath):
            self.readInput()
            return

        # Else download it
        url = "https://adventofcode.com/" + \
            str(self.year) + "/day/" + str(self.dayNumber) + "/input"
        result = requests.get(url, cookies={'session': self.sessionToken})
        if result.status_code == 200:
            with open(self.inputPath, 'w') as f:
                f.write(result.text)
        else:
            raise ConnectionError("Could not connect to AoC website to download input data. "
                                  "Error code {}: {}".format(result.status_code, result.text))

    def readInput(self):
        self.inputData = []

        # Opening filestream
        file = open(self.inputPath, "r")

        self.rawData = "".join(file.readlines())

        # Reading and appending each line to the inputData
        for line in file:
            line = line.replace('\n', '')
            self.inputData.append(line)

        # Closing filestream
        file.close()

    def writeOutput(self, *args):
        # Concats all the args into one string
        strToWrite = ""
        for arg in args:
            strToWrite += str(arg) + "\n"

        # Writes to console
        sys.stdout.write(strToWrite)

        # Writes to file
        file = open(self.outputPath, "w")
        file.write(strToWrite)
        file.close()

    def common(self):
        pass

    def part1(self):
        pass

    def part2(self):
        pass


class AOCDays:
    instance = None
    days = []

    def __init__(self):
        self.days = [0 for i in range(26)]

    def addDay(self, dayNumber, cls):
        self.days[dayNumber] = cls

    def getDay(self, dayNumber):
        return self.days[dayNumber]

    @classmethod
    def getInstance(cls):
        if not cls.instance:
            cls.instance = AOCDays()
        return cls.instance
