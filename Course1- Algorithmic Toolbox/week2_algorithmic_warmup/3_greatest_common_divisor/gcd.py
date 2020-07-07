# Uses python3
import sys

def gcd_naive(a, b):
    if(a == 0):
        return b
    else:
        return gcd_naive(b%a,a)

if __name__ == "__main__":
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    min_val=min(a,b)
    max_val=max(a,b)
    print(gcd_naive(min_val, max_val))
