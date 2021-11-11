"""
@Author: Shivam Mathur
@Date: 2021-11-09
@Last Modified by: Shivam Mathur    
@Last Modified time: 2021-11-09
@Title : A library for reading in 2D arrays of integers, doubles, or booleans from
         standard input and printing them out to standard output.

"""

def getArray(numberOfRows, numberOfColumns):
    """
    Description:
        this function generate 2d array
    Parameter:
        numberOfRows parameter is number of rows as input
        numberOfColumns parameter is number of columns as input 
    Return:
        this function returns a multi list
    """
    arrayList = [[0 for col in range(numberOfColumns)] for row in range(numberOfColumns)]

    try:
        for row in range(numberOfRows):
            for col in range(numberOfColumns):
                arrayList[row][col]= int(input())
        return arrayList
    except IndexError as e:
        print("Something wrong with index", e)

try:
    numberOfRows = int(input("Enter number of rows:"))
    numberOfColumns = int(input("Enter number of columns:"))
except Exception as e:
    print("Enter proper value", e)

arrayList = getArray(numberOfRows, numberOfColumns)
print(arrayList)