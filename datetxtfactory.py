
# 13.1 Write the current date as a string to the text file today.txt.
import  time
#needed this because I ran into errors when today did or did not exist, simple way to bypass that issue.
import os
def daDate():
    #If today file doesn't exist then execute
    if os.path.exists('today.txt') == False:
        #Creates today file to write to
        datimobj = open('today.txt', 'w')
        #Format for the today file
        now = "%m-%d-%Y"
        #Gets the current time and date
        t = time.localtime()
        #Formats the date into a string for the text file
        datimobj.write(time.strftime(now, t))
 
