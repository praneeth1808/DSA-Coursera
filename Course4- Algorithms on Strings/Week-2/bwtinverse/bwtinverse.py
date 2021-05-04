# python3
import sys
import math

def InverseBWT_fast(bwt):
    # write your code here
    last=[]
    counter={"$":0,"A":0,"C":0,"G":0,"T":0}
    for i in range(len(bwt)):
        symbol = bwt[i]
        last.append(symbol+str(counter[symbol]))
        counter[symbol] += 1
    first = []
    for key in ["$","A","C","G","T"]:
        for i in range(counter[key]):
            first.append(key+str(i))
    pos = 0
    text = ["A"]*len(last)
    first_to_last_map = dict(zip(first, last))
    nextSymbol="$0"
    for i in range(len(last)):
        text[i]=nextSymbol[0]
        nextSymbol=first_to_last_map[nextSymbol]
    return "".join(text[::-1])

def InverseBWT(bwt):
    # write your code here
    last=[]
    num=10**math.ceil(math.log10(len(bwt)))
    for i in range(len(bwt)):
        last.append(bwt[i]+str(num+i))
    first=sorted(last)
    pos=0
    text=""
    while True:
        currentNode = first[pos]
        text += currentNode[0]
        pos = last.index(currentNode)
        if pos == 0:
            return text[1:]

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT_fast(bwt))