import os #used to call 'clear' to clean the terminal window
import pandas as pd #used for the access to the excel file

clear = lambda: os.system('cls') #clear screen on windows system

clear() #call to clear screen

df = pd.read_excel (r'C:\Users\blake\Documents\GitHub\ebay-listing-tool\Master-Sheet.xlsx') #open and read teh excel file

f = open("myfile3.txt", "w")

bbdata = df.iat[2, 2] #Orange

f.write(bbdata)