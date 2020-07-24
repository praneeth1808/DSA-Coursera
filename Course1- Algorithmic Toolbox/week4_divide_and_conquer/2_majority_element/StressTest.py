# Uses python3
import sys
import random

def get_majority_element(a, left, right):
    try:
        if left == right:
            return -1
        if left + 1 == right:
            return a[left]
        #write your code here
        a.sort()
        lengthNeeded=(right+1)//2
        found=-1
        for i in range(lengthNeeded):
            if(a[i]==a[i+lengthNeeded]):
                return a[i]
        return found
    except:
        print(a)
        print((right+1)//2)
        print((right)//2)
        return -10
def get_majority_element_naive(a, left, right):
    ArrayDict={}
    for i in a:
        if( i in ArrayDict):
            ArrayDict[i]+=1
        else:
            ArrayDict[i]=1
    for x,y in ArrayDict.items():
        if(y>=right/2):
            return x
    return -1

def get_majority_element_2(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
#         print('now',a[left])
        return a[left]
#     print('call 1')
    left_elem = get_majority_element(a, left, (left+right+1)//2)
#     print('call 2')
    right_elem = get_majority_element(a, (left+right+1)//2, right)

    lcount = 0
#     print('left_elem',left_elem)
#     print('right_elem',right_elem)
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1

if __name__ == '__main__':
    mismatchFound=False
    while not mismatchFound:
        n = random.randint(0,10)
        ArrayFormed=[]
        while len(ArrayFormed)<n:
            RandCount=random.randint(0,10)
            RandInt=random.randint(0,10)
            ArrayFormed+=[RandInt]*RandCount
        res_1=get_majority_element(ArrayFormed, 0, len(ArrayFormed))
        res_2=get_majority_element_2(ArrayFormed, 0, len(ArrayFormed))
        res_3=get_majority_element_naive(ArrayFormed, 0, len(ArrayFormed))
        if(res_1!=res_3):
            print(ArrayFormed)
            print(res_1)
            print(res_3)
            mismatchFound=True
        else:
            print("OK!")
