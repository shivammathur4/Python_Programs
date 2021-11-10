"""
@Author: Shivam Mathur
@Date: 2021-11-08 
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-08 
@Title : Computes the prime factorization of N using brute force.

"""


import math

class Factors:
    def Factors(self):
        
        print("Enter Number : ")
        num = int(input())
        print("Prime factors for", num, "is")
        #Printing the factors of a given number until it is divided by 2.
        while num % 2 == 0:
                print("2")
                num = num / 2

        #If the given number is not even then this loop will print the remaining factors.
        for i in range(3, int(math.sqrt(num)+1)):
            while num % i == 0:
                print(i)
                num = num / i
            i+=2

        #If the remaining factor is greater than 2 it will be printing
        if num > 2:
            print(num)
        else:
            print()
nums = Factors()
nums.Factors()
