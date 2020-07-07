# python3


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
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_two(input_numbers))
