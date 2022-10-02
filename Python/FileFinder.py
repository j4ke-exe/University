#########################################################
#                Author: Jacob Garrison                 #
#                 Date: 2 October 2022                  #
#                    Class: ENTD261                     #
#                  Assignment: Week 5                   #
#########################################################
#  Description: This program will take a user input     #
#  and return the files that contain that input in the  #
#  current directory and output the results to a file   #
#  called Results.txt                                   #
#########################################################
#    To run this program, type the following in the     #
#    command line: python3 w5_jacob_garrison.py         #
#########################################################

import os, sys, time #Import modules

try: #Try to Open File
    filePath = input("Enter File Path: ") #Input File Path
    if filePath == "": #If No Input, Throw Error
        raise ValueError #Throw Error
    fileSize = int(input("Enter File Size in KB: ")) #Input File Size
    if fileSize == "": #If No Input, Throw Error
        print("Error: No File Size Entered") #Throw Error
    kb = fileSize * 1024 #Convert to Bytes
except: #If Error, Throw Error
    print("Invalid Input") #Throw Error
    sys.exit() #Exit Program

f=open('Results.txt', 'w') #Open Results.txt
for root, dirs, files in os.walk(filePath): #Walk through File Path
    for file in files: #For each file in the path
        path=os.path.join(root,file) #Get the path of the file
        calcSize=os.path.getsize(path) #Get the size of the file
        if calcSize >= kb: #If the file is larger than the input size
            f.write("File: " + path + "\n") #Write to Results.txt
            f.write("File Size: " + str(int(calcSize/1024)) + " KB" + "\n") #Write to Results.txt
            f.write("Date Created: " + time.ctime(os.path.getctime(path)) + "\n") #Write to Results.txt
            f.write("\n")
f.close() #Close Results.txt

print("Results sent to: " + filePath + "Results.txt") #Display File Path
