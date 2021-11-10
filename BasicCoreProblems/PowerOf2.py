
"""
@Author: Shivam Mathur
@Date: 2021-11-08 
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-08 
@Title = This program takes a command-line argument N and prints a table of the 
         powers of 2 that are less than or equal to 2^N.

"""

import math

Num = int(input('enter number from 1 to 31: '))
if Num > 31 and Num >= 0:
    print('please enter number from 1 to 31')
else:
    for i in range(Num):
        result = pow(2, i)
        print(result)
