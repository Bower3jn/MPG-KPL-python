"""
    converters.py
    This is a progran to convert MPG to KPL
    user is asked to eneter a value for MPG 
    and then the number is converted.
"""
# Declaring known constants
KPL = 1.609433     #kilometers per mile
GPL = 0.2641720524 #gallons per liter

def mpg2kpl(mpg) :
    """
        Converts MPG to KPL via the formula:
        KPL = MPG * KPM * GPL
    """
    return mpg * KPL * GPL

# ask the user to input an MPG value
mpg = input("What is the MPG")
#convert the imput in to a numeric (float value)
mpg = float(mpg)

# output the converted value rounded to 2 digets 
print(round(mpg2kpl(mpg), 2), "kpl")
 