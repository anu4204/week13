def findMaxInList(numberlist):
    if not numberlist:
        return None

    currentmax = numberlist[0]
    
    for number in numberlist:
        if number > currentmax:
            currentmax = number
    
    return currentmax

numberlist = [5, 12, 3, 8, 9]
print(findMaxInList(numberlist)) 