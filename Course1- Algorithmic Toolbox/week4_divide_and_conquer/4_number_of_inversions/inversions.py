# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions
def merge_sort(values):
    InvCount=0
    if len(values)>1:
        m = len(values)//2
        left = values[:m]
        right = values[m:]

        left = merge_sort(left)
        right = merge_sort(right)
        InvCount+=left[1]+right[1]
        left=left[0]
        right=right[0]
        values =[]
        while len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                InvCount+=len(left)
                right.pop(0)

        for i in left:
            values.append(i)
        for i in right:
            values.append(i)
    return [values,InvCount]
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    # print(get_number_of_inversions(a, b, 0, len(a)))
    print(merge_sort(a)[1])
