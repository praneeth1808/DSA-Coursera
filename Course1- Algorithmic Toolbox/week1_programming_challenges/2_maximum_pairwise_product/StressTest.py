# python3
import random


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_two(numbers):
    n=len(numbers)
    max_index_1=-1
    for i in range(n):
        if((max_index_1==-1) or (numbers[i]>numbers[max_index_1])):
            max_index_1=i
    max_index_2=-1
    for j in range(n):
        if((j!=max_index_1) and (max_index_2==-1 or numbers[j]>numbers[max_index_2])):
            max_index_2=j
    return numbers[max_index_1]*numbers[max_index_2]

if __name__ == '__main__':
    while True:
        n = random.randint(2,1000)
        a=[]
        for i in range(n):
            a.append(random.randint(0,100000))
        Res1=max_pairwise_product(a)
        Res2=max_pairwise_product_two(a)
        if(Res1!=Res2):
            print(a)
            print ("Res 1: ",Res1,"\nRes 2: ",Res2)
            break
        else:
            print(a)
            print("OK")