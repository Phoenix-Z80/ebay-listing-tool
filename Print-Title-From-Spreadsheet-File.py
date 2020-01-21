import os #used to call 'clear' to clean the terminal window
import pandas as pd
import time

clear = lambda: os.system('cls') #clear screen on Windows System

clear() #call to clear screen

df = pd.read_excel (r'C:\Users\blake\Documents\GitHub\ebay-listing-tool\Master-Sheet.xlsx') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'

#bbdata = df.iloc(0)

#print type(df.iloc[1])

#print (bbdata)

#df.iloc[0]['More Details']

#example data set...
#Ref  Title (No Specials)  More Details
#1    White                Purple
#2    Black                Green
#3    Pink                 Orange

bbdata = df.iat[0, 0] #1
print(bbdata)
bbdata = df.iat[1, 0] #2
print(bbdata)
bbdata = df.iat[0, 1] #White
print(bbdata)
bbdata = df.iat[2, 2] #Orange
print(bbdata)
#Starting form A2 first value = down, second value = accross

#time.sleep(5.5)    # pause 5.5 seconds
#print("something")