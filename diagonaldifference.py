#take in 2d array, and input what a variable 
def diagonalDifference(arr):
    try:
        left = right = 0
        n = len(arr)
        i = j = 0
        k = l = n - 1
        while i <= n - 1 and j <= n - 1 and k >= 0 and l >= 0:
            left += arr[i][j]
            right += arr[k][l]
            if(i == n - 1 and j == n - 1 and k == 0 and l == 0):
                break
            i += 1
            j += 1
            k -= 1
            l -= 1
        return abs(left - right)
    except TypeError:
        print("I can't do this, I need a 2d array with only integers")