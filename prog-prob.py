'''
Author: GROUP 4
Date: 09/09/2022
Program Description: Programming Problems 1 and 2
Filename: prog-prob.py
'''

a_num = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 15]
a = len(a_num)
  
getsum = sum(a_num)
mean = getsum / a
  
print("The Mean is: " + str(mean))

b_num = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10, 7]
b = len(b_num)
b_num.sort()
  
if b % 2 == 0:
    median1 = b_num[b//2]
    median2 = b_num[b//2 - 1]
    median = (median1 + median2)/2
else:
    median = b_num[b//2]
print("The Median is: " + str(median))

from collections import Counter

c_num = [1, 2, 3, 4, 5, 5, 6, 7, 7, 7, 9 ,8, 10, 10, 10]
c = len(c_num)
  
data = Counter(c_num)
getmode = dict(data)
mode = [k for k, v in getmode.items() if v == max(list(data.values()))]
  
if len(mode) == c:
    getmode = "There is no mode"
else:
    getmode = "The Mode is / are: " + ', '.join(map(str, mode))
      
print(getmode)