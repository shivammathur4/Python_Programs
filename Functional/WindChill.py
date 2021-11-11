
"""
@Author: Shivam Mathur
@Date: 2021-11-09
@Last Modified by: Shivam Mathur    
@Last Modified time: 2021-11-09
@Title : Finding wind chill from velocity and temperature.

"""

import math
class WindChill:

    def WindChill(self,temp, velocity):

        """
    Description:
        Function generates wind chill from velocity and temperature
    Parameter:
        temp: temp input is taken
        velocity:  velocity input is taken
    Return:
        array output
    """

        power = math.pow(velocity, 0.6)
        windChill= 35.47 + 0.6215 * temp + (0.4275 * temp + 35.75) * power
        print("Wind Chill of weather")
        print(windChill)


if __name__ == '__main__':
        try:
            temp = int(input("enter temp below 50 in fahrenheit : "))
            velocity = int(input("enter velocity in range of 3m/s and  120m/s : "))
            wind_chill=WindChill()
            wind_chill.WindChill(temp, velocity)

        except ValueError:
                print("check the input")