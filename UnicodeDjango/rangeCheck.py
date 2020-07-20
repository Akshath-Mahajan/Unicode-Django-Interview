def checkBits(start, end):
    '''
    Function - checkBits(start, end)
    Parameters: 1) start - Denotes start point of range
                2) end - Denotes end point of range
    
    Returns: Dictionary 'result' which has keys as numbers in the range
    and values are booleans.
    For each key: 
    The value being True implies there are two consecutive 1's in the binary equivalent for that key 
    The value being False implies there are no consecutive 1's in the binary equivalent for that key
    
    Time Complexity = O(end-start)
    '''
    result = {}
    #If no two consecutive bits in a number 'i' are set, i&(i>>1) evaluates to 0
    for i in range(start, end):
        result[i] = bool(i&(i>>1)) 
    return result
