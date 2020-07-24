# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    a.sort()
    lengthNeeded=(right+1)//2
    LoopArrayLength=right//2
    found=-1
    for i in range(lengthNeeded):
        if(a[i]==a[i+LoopArrayLength]):
            return a[i]
    return found

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
