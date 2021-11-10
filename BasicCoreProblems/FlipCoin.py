"""
@Author: Shivam Mathur
@Date: 2021-11-08 
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-08 
@Title : Flip Coin and print percentage of Heads and Tails

"""

import random
class FlipCoin:
    def printing(self):
        print("Enter no of time to flip coin")
        # taking input from the user no of times to flip the coin
        num = int(input())
        head=0
        tail=0

        if num!=0:
            for i in range(0, num):
                # taking random number for each time of the loop running
                x = random.random()
                # if random number is less than 0.5 it counted as Tails else false
                if x<0.5:
                    head=head+1
                else:
                    tail=tail+1
            # finding the percentage of heads and tails
            headPercentage = head*100/num
            tailPercentage = tail*100/num
            print("Head Percentage = ", headPercentage, "%")
            print("Tail Percentage = ", tailPercentage, "%")
        else:
            print("You have entered 0 Value, it is not possible")
# creating object for the class and calling the method
flipcoin = FlipCoin()
flipcoin.printing()