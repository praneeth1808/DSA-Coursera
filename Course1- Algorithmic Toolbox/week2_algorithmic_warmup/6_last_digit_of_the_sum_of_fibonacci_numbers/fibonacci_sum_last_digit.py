# Uses python3
import sys

def fibonacci_sum_naive(n):
    Series_sum=[0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]
    return Series_sum[n%len(Series_sum)]
# def calc_fib(n):
#     FebSeries=[]
#     FebSeries.append(0)
#     FebSeries.append(1)
#     for i in range(2,n+1):
#         FebSeries.append(FebSeries[i-1]+FebSeries[i-2])
#     return FebSeries[n]

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum_naive(n))
    # Temp=[0,1]
    # Temp_2=[0,1]
    # for i in range(2,100):
    #     Temp.append(calc_fib(i)%10)
    #     Temp_2.append((Temp_2[i-1]+calc_fib(i)%10)%10)
    # print(Temp)
    # print(Temp_2)
