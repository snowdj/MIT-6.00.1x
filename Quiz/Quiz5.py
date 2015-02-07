def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Get the length of both strings
    lenS1 = len(s1)
    lenS2 = len(s2)
    result = ""
    extra = ""
    
    # Check if both strings are empty
    #if lenS1==0 and lenS2==0:
    #    return result
    
    # Determine extra string to add to end
    if lenS1 > lenS2:
        extra = s1[lenS2:]
    elif lenS1 < lenS2:
        extra = s2[lenS1:]
    
    for char in range(min(lenS1,lenS2)):
        result += s1[char]+s2[char]
    
    return result + extra