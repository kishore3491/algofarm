
def convert(str):
    """
    :type str: str
    :rtype: int
    """
    # Group1 = +~/- sign
    # Group2 = [0-9]+
    # Group3 = . (if exists)
    # Group4 = [0-9]+
    validation = {45: True, 46: True, 32: True, -32: False}
    res = 0
    decRes = 0
    decimal = False
    negative = False
    spaceExpired = False
    numPos = 0
    INT_MAX = 2147483647

    for c in reversed(str):
        val = ord(c)
        # Integer overflow check.
        if numPos > 9 and val > 2:
            return INT_MAX

        if val in validation:
            # do something
            if val == 46:
                # Set sign and space to false
                validation[45] = False
                validation[32] = False
                decimal = True
            elif val == 45:
                validation[32] = False
                negative = True


        elif val in range(48, 58):
            # append
            if decimal:
                # append after zeros
                decRes = float(res/(10**numPos))
                res = 0
                # Reset decimal
                decimal = False
            else:
                res += (val - ord('0'))*(10**numPos)
            numPos += 1
        else:
            print ('Val out of range.')
            return 0

    # If decimal, add decimal result.
    if decimal:
        res += decRes

    if negative:
        return -res
    else:
        return res

if __name__ == "__main__":
    print (convert('-144.60'))
