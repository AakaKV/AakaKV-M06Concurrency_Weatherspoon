#ran into errors so I Modulated these 2 parts of CH 13 to make it manageable for fixing it.
from datetxtfactory import *
# 13.2 Read the text file today.txt into the string today_string.
daDate()
#Format for the strip time function
formatTime = "%m-%d-%Y"
#Checks if the today.txt file exists so an error doesn't occur
if os.path.exists('today.txt') == True:
    #reads the today file
    stringday= open('today.txt', 'r')
    #reads Line
    today_string = stringday.readline()
    #Prints the formatted date before it is stripped
    print("Today is ", today_string)
    #Prints the date that is stripped
    print(time.strptime(today_string,formatTime))
    #closes the today file
    stringday.close()
