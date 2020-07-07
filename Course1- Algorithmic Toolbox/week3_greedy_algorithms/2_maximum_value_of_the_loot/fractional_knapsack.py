# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    length=len(weights)
    A=[0]*length
    # write your code here
    list_values=[]
    for i in range(length):
        list_values.append({
            "weight":weights[i],
            "value":values[i],
            "VPU":values[i]/weights[i]
        })
    SortedList = sorted(list_values, key=lambda x: x['VPU'], reverse=True)
    for i in range(length):
        if capacity==0:
            return value
        a=min(SortedList[i]['weight'],capacity)
        value+=a*(SortedList[i]['VPU'])
        A[i]+=a
        capacity-=a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
