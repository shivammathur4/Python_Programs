
"""
@Author: Shivam Mathur
@Date: 2021-11-10
@Last Modified by: Shivam Mathur
@Last Modified time: 2021-11-10
@Title : Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.

"""

import random

class CouponNumbers:

    def inputNumberOfCoupons(self):
        """ 
        Description:
            Taking input from user for number of coupons
        Return:
            numberOfCoupons
        """
        while True:
            try:
                numberOfCoupons = int(input("Enter number of distinct coupons: "))
                if numberOfCoupons <= 1:
                    print("number of coupons should be positive integer")
                    continue
                break
            except Exception as e:
                print(e)
        return numberOfCoupons

    def findDistinctCoupons(self, totalCoupons):
        """ 
        Description:
            Finding distinct coupons using random numbers
        Return:
            return all distinct coupon numbers
        """
        distinctNumbers = []
        while len(distinctNumbers) < totalCoupons:
            rand = random.randint(1, totalCoupons)#Generate random number between 1 to totalcoupons
            if rand not in distinctNumbers:
                distinctNumbers.append(rand)
        return distinctNumbers

if __name__ == "__main__":
    """Main Method """
    couponNumbers = CouponNumbers()
    numbersOfCoupons = couponNumbers.inputNumberOfCoupons()
    distinctCoupons = couponNumbers.findDistinctCoupons(numbersOfCoupons)
    print("All Distinct coupons are: ", distinctCoupons)