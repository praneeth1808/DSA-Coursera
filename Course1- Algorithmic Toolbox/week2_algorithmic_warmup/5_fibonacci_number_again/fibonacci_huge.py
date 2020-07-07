# Uses python3
import sys

def calc_fib_last_digit(n,m):
    FebSeries=[]
    FebSeries.append(0)
    FebSeries.append(1)
    for i in range(2,n+1):
        CurrentDigit=(FebSeries[i-1]+FebSeries[i-2])%m
        if CurrentDigit==1 and FebSeries[i-1]==0:
            FebSeries.pop()
            break
        else:
            FebSeries.append(CurrentDigit)
    return FebSeries[n%len(FebSeries)]
if __name__ == '__main__':
    # input = sys.stdin.read();
    n, m = map(int, input().split())
    print(calc_fib_last_digit(n, m))
