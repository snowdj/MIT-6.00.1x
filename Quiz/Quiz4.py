def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Check the special case of x = 1
    result = 0
    if x==1:
        return result
    else:
        while True:
            if b**result == x:
                return result
            elif b**result < x:
                result += 1
            elif b**result > x:
                return result-1               
                