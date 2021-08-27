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
        elif(a[0] < b[0]):
            bPoints += 1
        else:
            pass
        if(a[1] > b[1]):
            aPoints += 1
        elif(a[1] < b[1]):
            bPoints += 1
        else:
            pass
        if(a[2] > b[2]):
            aPoints += 1
        elif(a[2] < b[2]):
            bPoints += 1
        else:
            pass
        return [aPoints, bPoints]
    except ValueError:
        print("I can't use this array, it needs to be three numbers")
    except IndexError:
        print("There's not enough of an input here, I need three numbers, not 0, 1 or 2")
    
#test cases
#gets [0, 3]
compareTriplets([1, 2, 3],[4, 5, 6])
#gets [1, 0]
compareTriplets([1, 2, 3],[1, 2, 1])
#gets ValueError
compareTriplets(["a,", "b", "c"],["d", "e", "f"])
#gets IndexError
compareTriplets([1, 2, 3][4, 5]) 
#gets [0, 3], completely ignores anything else in the array other than the first 3 variables
compareTriplets([1, 2, 3, 2, 1],[4, 5, 6, 7]) 
