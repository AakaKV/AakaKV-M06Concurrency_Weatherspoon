# Use multiprocessing to create three separate processes. Make each one wait a random
# number of seconds between zero and one, print the current time, and then exit.
import random
import multiprocessing
import os
import time
def getTime(pnum):
    #Format for the today file
    now = "%m-%d-%Y"
    #Gets the current time and date
    t = time.localtime()
    print(f"Process {pnum} says the time is:", time.strftime(now, t))

if __name__ == "__main__":
getTime(3)
for n in range(3):# this makes 3 processes
    getTime(n)
    proTime = multiprocessing.Process(target=getTime,
        args=n)
    proTime.start()
