"""
@Author: Shivam Mathur
@Date: 2021-11-09
@Last Modified by: Shivam Mathur    
@Last Modified time: 2021-11-09
@Title : Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)

"""

import math

class Quardatic:

    def findRoots(self,num1, num2, num3):
        # If a is 0, then equation is
        # not quadratic, but linear
        if num1 == 0:
            print("Invalid")
            return -1
        delta = num2 * num2 - 4 * num1 * num3
        # sqrt() function is used to return the square root of a positive number.
        # abs() function returns the absolute value of the number.
        sqrt_val = math.sqrt(abs(delta)) 

        if delta > 0:
            print("Roots are real and different ")
            print((-num2 + sqrt_val) / (2 * num1))
            print((-num2 - sqrt_val) / (2 * num1))
        elif delta == 0:
            print("Roots are real and same")
            print(-num2 / (2 * num1))
        else:  # delta<0
            print("Roots are complex")
            print(- num2 / (2 * num1), " + i", sqrt_val)
            print(- num2 / (2 * num1), " - i", sqrt_val)


if __name__ == '__main__':
    try:
        num1 = int(input("Enter the First Integer: "))
        num2 = int(input("Enter the Second Integer: "))
        num3 = int(input("Enter the Third Integer: "))

        # Function call
        quardatic=Quardatic()
        quardatic.findRoots(num1,num2,num3)

    except ValueError:
            print("check the input ")