# Uses python3
import sys

def binary_search(a, x,left,right):

    while left<=right:
        mid= left+int((right-left)/2)
        # print("Left :",left,"Right :",right,"Mid :",mid)
        if(a[mid]==x):
            return mid
        elif(a[mid]>x):
            return binary_search(a,x,left,mid-1)
        else:
            return binary_search(a,x,mid+1,right)
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x,0,len(a)-1), end = ' ')
