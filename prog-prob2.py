'''
Author: GROUP 4
Date: 09/09/2022
Program Description: Programming Problem 2
Filename: prog-prob2.py
'''

enterfile = input("Please enter the file name: ")
file = open(enterfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1
print("The number of lines in this text file is", linecount)
while True:
    linenum = 0
    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thanks for using the program!")
            break