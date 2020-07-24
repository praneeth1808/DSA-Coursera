# Uses python3
import sys
import random
def partition3_o(a, l, r):
    pivot_value = a[l]
    p_l = i = l
    p_e = r
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
    return p_l,p_e
def partition3(a, l, r):
    #write your code here
    x=a[l]
    m1=l
    m2=r
    for i in range(l,r+1):
        if(a[i]==x):
            pass
        elif(a[i]<x):
            a[i],a[m1]=a[m1],a[i]
            m1+=1
        elif(a[i]>x):
            a[i],a[m2]=a[m2],a[i]
            m2-=1
    return m1,m2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1,m2=partition3_o(a,l,r)
    # print("m1 : ",m1,"m2 : ",m2)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
