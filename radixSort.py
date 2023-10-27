

def getDigit(n,pos):
    return (n//10**pos)%10
def TotalDigits(n):
    return len(str(n))

def InsertionSort(arr,pos):
    for i in range(len(arr)):
        key = arr[i]
        keyDigit = getDigit(key,pos)
        j = i - 1
        while getDigit(arr[j],pos)>keyDigit and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def RadixSort(arr):
    print(arr)
    minVal = min(arr)
    maxVal = max(arr)
    for i in range(len(arr)):
        arr[i]+=abs(minVal)
    print(arr)
    for i in range(TotalDigits(maxVal)+1):
        arr = InsertionSort(arr,i)
    print(arr)
    for i in range(len(arr)):
        arr[i]-=abs(minVal)
    return arr

A = [1,5,7,9,4,6,2,4,678,21,4,-2,-2,0,55]
print(RadixSort(A))

