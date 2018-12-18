def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L(0)
    max = L(0)
    if len(L) == 1:
        return (min, max)
    else:
        for i in L:
            if i < min:
                min = i
            elif i > max:
                max = i
        return (min, max)
