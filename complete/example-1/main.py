"""
This module contains functions to validate if code is a valid universal product code
"""

def isUniversalProductCode(code):
    """Checks if code is a valid universal product code

    A valid product code has its contol algharism (first algharism) calculated by: 
    1) summing the values at odd positions of the code and multiplying the result by 3;
    2) adding to the triple of the sum of the odd positioned values the sum of the algharisms at even positions;
    3) Subtract to the closest multiple of 10 greater or equal to the previously calculated sum, the sum.

    Args:
        code (str): string containing a code that needs to be validated.
    
    Returns:
        bool: returns true if code is a valid universal product code

    >>> isUniversalProductCode('9788679912077')
    True
    >>> isUniversalProductCode('9789679912077')
    False
    >>> isUniversalProductCode('abcdefg')
    Code string must contain a number
    """

    try:
        int(code)
    except ValueError:
        print("Code string must contain a number")
        return 

    oddSum = 0
    evenSum = 0 

    control,rest = int(code[0]),code[1::]

    for position in range(len(rest)):
        if position % 2 == 0:
            oddSum += int(rest[position])
        else:
            evenSum += int(rest[position])
    
    temp_sum = oddSum * 3 + evenSum

    return control == (closestMultipleOf10EGTo(temp_sum) - temp_sum)
    

def closestMultipleOf10EGTo(number):
    """Finds the closes multiple of ten which is greater or equal to a given number

    Args:
        number (int): number for which to find the closest multiple of then, greater of equal to it

    Returns:
        int: multiple of ten greater or equal to number

    >>> closestMultipleOf10EGTo(150)
    150
    >>> closestMultipleOf10EGTo(151)
    160
    """
    if number % 10 == 0:
        return number
    else:
        dividend = number // 10
        return (dividend+1) * 10
    

if __name__=='__main__':
    import doctest
    doctest.testmod()