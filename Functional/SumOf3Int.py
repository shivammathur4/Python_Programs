"""
@Author: Shivam Mathur
@Date: 2021-11-09
@Last Modified by: Shivam Mathur    
@Last Modified time: 2021-11-09
@Title : Sum of three Integer adds to ZERO

"""

def findTriplets(elementList, numberOfElements):
    """
    Description:
        this function finds triplet with sum 0
    Parameter:
        elementList consist this elements for triplets
        numberOfElements represents size of elementList 
    """
    FOUND = False
    for i in range(0, numberOfElements-2):
     
        for j in range(i+1, numberOfElements-1):
         
            for k in range(j+1, numberOfElements):
             
                if (elementList[i] + elementList[j] + elementList[k] == 0):
                    print(elementList[i], elementList[j], elementList[k])
                    FOUND = True

    if (FOUND == False):
        print("no triplet with sum zero exist")
 
elementList = []

try:
    numberOfElements = int(input("Enter size:"))
except Exception as e:
    print("Enter proper value", e)

for element in range(numberOfElements):
    elementList.append(int(input("Enter the elements:")))

findTriplets(elementList, numberOfElements)