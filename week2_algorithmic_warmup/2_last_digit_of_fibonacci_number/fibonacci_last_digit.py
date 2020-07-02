# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    Feb_series=[0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
    return Feb_series[n%60]

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
