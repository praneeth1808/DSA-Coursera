# Uses python3
import sys


def gcd_alg(a, b):
    if(a == 0):
        return b
    else:
        return gcd_alg(b%a,a)
def lcm_naive(a, b):
    gcd=gcd_alg(a,b)
    return a*b//gcd
if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    min_val=min(a,b)
    max_val=max(a,b)
    print(lcm_naive(min_val, max_val))

