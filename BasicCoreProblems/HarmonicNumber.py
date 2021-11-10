
"""
@Author: Shivam Mathur
@Date: 2021-11-08 
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-08 
@Title : Print the Nth Harmonic Value.

"""

number = int(input('Enter the value of N:'))

if number <= 0:
    print('Please enter value greater then 0')
else:
    Result = 0
    for i in range(1, number + 1):
        #The Range between 1 to n+1
        # Every time of the loop taking the sum of the next harmonic number
        harmonic = 1/i
        Result += harmonic
        print("Nth Harmonic Value ", Result)
