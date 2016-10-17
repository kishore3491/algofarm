
def convert(word):
    """
    :type str: str
    :rtype: int
    """
    """
    Step 1: Strip trailing and leading white spaces and
            set spaceExpired to True
    Step 2: Use a validation map to disallow duplicate pointers
            like ., ' ', +/- etc. These values should be allowed only once.
    Step 3: Check for decimal pointers
    Step 4: Check for negative pointers
    Step 5: Disallow any numbers after encounter with +/- sign.
    """
    # Group1 = +~/- sign
    # Group2 = [0-9]+
    # Group3 = . (if exists)
    # Group4 = [0-9]+

    # Validation vector, true for allowed.
    # 43 = +, 45 = -, 46 = ., 32 = ' '
    validation = {43: True, 45: True, 46: True, 32: True}
    res = 0.0
    decRes = 0.0
    decimal = False
    negative = False
    numPos = 0
    zero = ord('0')
    INT_MAX = 2147483647
    numsAllowed = True

    # Remove leading and trailing white spaces.
    i = 0
    j = len(word) - 1
    while (i < j):
        if word[i] == ' ':
            i += 1
        elif word[j] == ' ':
            j -= 1
        else:
            validation[32] = False
            break;

    for c in reversed(word[i:j+1]):
        val = ord(c)
        # Integer overflow check.
        if numPos > 9 and (val - zero) > 2:
            return INT_MAX

        # Check if validation passes.
        if val in validation and validation[val] == True:
            if val == 46:
                # Set sign allowed to false
                validation[46] = False
                decimal = True
            elif val == 45:
                validation[45] = False
                negative = True
                numsAllowed = False
            elif val == 32:
                return 'Invalid space in between characters.'
            elif val == 43:
                validation[43] = False
                numsAllowed = False


        elif val in range(48, 58) and numsAllowed:
            # append
            if decimal:
                # append after zeros
                decRes = float(res/(10**numPos))

                # Important: Reset numPos to 0
                numPos = 0
                res = (val - zero)*(10**numPos)
                # Reset decimal
                decimal = False

            else:
                res += (val - zero)*(10**numPos)
            numPos += 1

        else:
            return 'Invalid'

    # add decimal result, if any.
    res += decRes

    if negative:
        return -res
    else:
        return res

if __name__ == "__main__":
    print (convert(' -144.60  '))
    print (convert(' 144.60  '))
    print (convert(' -144.606'))
    print (convert(' -144.60*'))
    print (convert(' -144. 60  '))
    print (convert(' -14+4.60  '))
    print (convert('-144'))
    print (convert('1.0'))
    print (convert('1'))
