import os #used to call 'clear' to clean the terminal window
import pandas as pd #used for the access to the excel file

clear = lambda: os.system('cls') #clear screen on windows system

clear() #call to clear screen

df = pd.read_excel (r'C:\Users\blake\Documents\GitHub\ebay-listing-tool\Master-Sheet.xlsx') #open and read teh excel file

f = open("myfile5.txt", "w")

value = int(input('Enter in row required?\n(0 writes White - Purple)\n')) #get value and store in 'value' vairable

#bbdata = df.iat[2, 2] #Orange

#f.write(bbdata)

f.write(df.iat[(value), 1])
f.write(" - ")
f.write(df.iat[(value), 2])