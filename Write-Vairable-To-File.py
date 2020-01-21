import os #used to call 'clear' to clean the terminal window

clear = lambda: os.system('cls') #clear screen on Windows System

clear() #call to clear screen

f = open("myfile2.txt", "w")

i = "floaty"

f.write(i)



#for i in range(10):
#	if i < 9:
#		f.write("This is line %d\r" % (i+1))
#	else:
#		f.write("This is line %d no cr at the end of this line" % (i+1))
#
#f.write("\r\rThis is a brand new line")