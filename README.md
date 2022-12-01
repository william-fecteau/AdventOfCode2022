# Python Framework for Advent Of Code 

## What is Advent Of Code?
Advent of code is a series of coding challenges in the form of an advent calendar : One challenge divided in two parts per day from December 1rst up until December 25th [https://adventofcode.com/](https://adventofcode.com/)

## Why this framework?
I created this python AoC framework to handle every basic action that you need to do every single day like : 

- Creating your daily solution file that can be ran automatically (from a template)
- Downloading your inputs if its not already there
- Automatically reading the current day input and putting it into a variable that you can use everyday withtout touching your file system
- Executing your solution by part one day at a time or all days at the same time
- Timing the execution of your program to compare run times

## Example usage
- https://github.com/william-fecteau/AdventOfCode2020
- https://github.com/william-fecteau/AdventOfCode2021
- https://github.com/william-fecteau/AdventOfCode2022

## Prerequisites
For it to work, you need to have two packages installed ```requests``` and ```python-dotenv``` which you can install using this command : 
```pip install -r requirements.txt```
*Of course you need to have pip installed also*

## Installation
1. Clone the repo
2. Install the requirements ```pip install -r requirements.txt```
3. Create a ```.env``` file at the root of the repo
4. In this ```.env``` file, add the two following variables and change their values for your need :
```
AOC_SESSION_COOKIE=yourSessionCookie
AOC_YEAR=2021
```
*Note: You can get your session cookie by logging to the AoC website and looking in the cookies of one of your requests using dev tools. This cookie will be needed to download your input automatically*

## Framework flow
A day file is created with this template :
```
from utils.aoc_utils import AOCDay, day

@day(0)
class DayTemplate(AOCDay):
    def common(self):
        #print(self.inputData)
        #print(self.rawData)
        return 0

    def part1(self):
        return 0
    
    def part2(self):
        return 0
```
*Note: ```self.inputData``` contains the list of every line from your input (Splitted on '\n') and ```self.rawData``` contains all the data in a single string (Including all the '\n')*.


## How to use it
### Start a day
To start a day, use this command : ```python3 main.py <dayNumber>```


If its not already there, this will create your day file for you to program in.


Your day file will be in ```./days/day<dayNumber>.py``` (This is where you program!)

### Run a day
To run a day, use this command : ```python3 main.py <dayNumber>``` (Notice it's the same command as how to start a day)


The input file will be downloaded in ```./inputs/day<dayNumber>.txt``` (Normally you don't need to touch this file! It will be parsed automatically)


After downloading the input, it will run your code and produce the output in the console and at ```./outputs/day<dayNumber>.txt```
