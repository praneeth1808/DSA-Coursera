# python3
import sys

def BWT(text):
    length = len(text)
    text=2*text
    matrix=[]
    for i in range(length):
        matrix.append(text[i:i+length])
    matrix.sort()
    BWT=""
    for i in matrix:
        BWT+=i[-1]
    return BWT

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))