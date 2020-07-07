# Uses python3
import sys

def get_change(m):
    #write your code here
    coins=[10,5,1]
    count=0
    for i in coins:
        if m==0:
            return count
        count+=m//i
        m=m%i
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
