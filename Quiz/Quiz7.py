def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    m = (6, 9, 20)
    lst = [m[0], m[1], m[2], m[0]+m[1], m[0]+m[2], m[1]+m[2], m[0]+m[1]+m[2]]
    
    def total(tup):
        return sum(p*q for p,q in zip(tup,m))
    
    # function to check if n is divisible by base combinations of 6, 9, 20
    def checkMod(x):
        result = False   
        calc = [x%z for z in lst]
        for each in calc:
            if each == 0:
                result = True
                break
        return result
    
    # fucntion to calculate the difference between a number and the lst
    def diffLst(x):
        result = [x-z for z in lst]
        return result
            
    result = False
    # Check if multiple of 6, 9 or 20 and return true if so
    if checkMod(n)==True:
        result = True
        return result
    elif n>20:
        # calculate the difference between n and each item in lst
        diff = diffLst(n)
        # Check if differences pass the checkMod
        for each in diff:
            test = checkMod(each)
            if test == True:
                result = True
                break                                    
    return result