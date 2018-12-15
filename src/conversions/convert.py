def convertDecimalToHexadecimal(base10Num):
    # make a dictionary
    largerDigits = {10: 'A',
                    11: 'B',
                    12: 'C',
                    13: 'D',
                    14: 'E',
                    15: 'F'
                    }
    # if the number in base 10 is 0-9, just convert it to a string
    # if the number is >9 convert it to a letter using the dictionary
    if base10Num < 10:
        out = str(base10Num)
    else:
        out = largerDigits[base10Num]
    return out

