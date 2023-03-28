#Example: writing data in to the file
# open in writing mode and store it in a variable File
'''f=open("C:\\Users\\tajudeen.busari\\pythonDemoFile\\file.txt",  "w") #i added the \\ cos it was given error in my code
f.write("this is my file\n")        #"\n" makes the second statemnet to start from the suceeding line
f.write("this is my file\n")
f.write("this is my file\n")
f.write("this is my file\n")
f.write("this is my file\n")
f.close()
print("programme completed")'''

#Example: read data and print in the console window
'''f=open("C:\\Users\\tajudeen.busari\\pythonDemoFile\\file.txt",  "r")
#print(f.read())
print(f.readline()) #reads just one single line
f.close()'''

#Example: appending data into txt file
f=open("C:\\Users\\tajudeen.busari\\pythonDemoFile\\file.txt",  "a")
f.write("\this is another line\n")
f.write("this is another line\n")
f.close()
print("success")



