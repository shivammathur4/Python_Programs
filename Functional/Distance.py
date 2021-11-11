"""
@Author: Shivam Mathur
@Date: 2021-11-09
@Last Modified by: Shivam Mathur    
@Last Modified time: 2021-11-09
@Title : Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function.

"""

import math
class Distance:

    # Distance is used for finding distance between 2 points
    def distance(self,ponitA, pointB):
        
        """
    Description:
        Function generates difference using maths formula
    Parameter:
        ponitA: point 1
        ponitB: point 2
    Return:
        distance between 2 point
    """
        
        dist = math.sqrt((ponitA ** 2 + ponitB ** 2))
        print(dist)
        # here difference is returned
        return dist

if __name__ == '__main__':
        try:
            ponitA = int(input("Enter Number 1 : "))
            ponitB = int(input("Enter Number 2 : "))
            distance=Distance()
            distance.distance(ponitA, ponitB)

        except ValueError:
            print("check the input ")