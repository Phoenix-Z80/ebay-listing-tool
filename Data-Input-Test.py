import os #used to call 'clear' to clean the terminal window

clear = lambda: os.system('cls') #clear screen on Windows System

clear() #call to clear screen

value = input('Hello! What is your value?\n') #get value and store in 'value' vairable

print ('You typed in the value {0}.'.format(value)) #'value' is the vairable name. {0} is the location where to put this in the print command.