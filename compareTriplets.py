#see whether player a or b got more points by comparinfg array items
def compareTriplets(a, b):
    try:
        a[0] = float(a[0])
        a[1] = float(a[1])
        a[2] = float(a[2])
        b[0] = float(b[0])
        b[1] = float(b[1])
        b[2] = float(b[2])
        aPoints = 0
        bPoints = 0
        if(a[0] > b[0]):
            aPoints += 1
        else:
            bPoints += 1
        if(a[1] > b[1]):
            aPoints += 1
        else:
            bPoints += 1
        if(a[2] > b[2]):
            aPoints += 1
        else:
            bPoints += 1
        return [aPoints, bPoints]
    except:
        print("I can't use this array, it needs to be three numbers")
    
