import sys
import os
import shutil

from dotenv import load_dotenv

from days import *
from utils.aoc_utils import AOCDay, AOCDays


if __name__ == "__main__":
    load_dotenv()  # take environment variables from .env.
    
    year = os.getenv('AOC_YEAR')
    sessionToken = os.getenv('AOC_SESSION_COOKIE')

    # Getting parameters
    runAll = False
    dayNumber = 1
    if len(sys.argv) >= 2:
        try:
            if sys.argv[1] == "all":
                runAll = True
            else:
                dayNumber = int(sys.argv[1])
        except Exception:
            print("{} - Run aoc solutions".format(sys.argv[0]))
            print("Usage: {} [day]".format(sys.argv[0]))
            sys.exit(1)
    else:
        print("{} - Run aoc solutions".format(sys.argv[0]))
        print("Usage: {} [day]".format(sys.argv[0]))
        sys.exit(1)

    # Validation
    relPath = "/days/day" + str(dayNumber) + ".py"
    if dayNumber <= 0 or dayNumber > 25:
        print("Day must be between 0 and 25")
        sys.exit(1)
    # If day file does not exist, create it
    elif not os.path.exists(os.getcwd() + relPath):
        # Copying template file
        shutil.copy(os.getcwd() + "/days/_template.py", os.getcwd() + relPath)
        
        # Renaming template
        fin = open(os.getcwd() + relPath, "rt")
        data = fin.read()
        data = data.replace("@day(0)", "@day(" + str(dayNumber) + ")").replace("DayTemplate", "Day" + str(dayNumber))
        fin.close()

        # Overriding day file
        fin = open(os.getcwd() + relPath, "wt")
        fin.write(data)
        fin.close()

        print("Day "+ str(dayNumber) + " created! glhf")

    # Else we run it normally
    else:
        if runAll:
            daysRun = [x+1 for x in range(25)]
        else:
            daysRun = [dayNumber]
    

        for dayNum in daysRun:
            # Getting the good days instance
            curDay : AOCDay = AOCDays.getInstance().getDay(dayNum)
            
            try:
                inst = curDay(year, dayNum, sessionToken)
                inst.run()
            except Exception as e:
                print(e, file=sys.stderr)
                sys.exit(1)