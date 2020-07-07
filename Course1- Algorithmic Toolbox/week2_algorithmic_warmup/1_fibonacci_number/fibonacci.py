# Uses python3
def calc_fib(n):
    FebSeries=[]
    FebSeries.append(0)
    FebSeries.append(1)
    for i in range(2,n+1):
        FebSeries.append(FebSeries[i-1]+FebSeries[i-2])
    return FebSeries[n]

n = int(input())
print(calc_fib(n))
