# Uses python3
import sys
import math
def optimal_summands(n):
    summands = []
    #write your code here
    max_range=int(math.sqrt(2*n + 0.25)-0.5)
    sum = int(max_range*(max_range+1)*0.5)
    summands=[*range(1,max_range),max_range+n-sum]
    return summands
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
