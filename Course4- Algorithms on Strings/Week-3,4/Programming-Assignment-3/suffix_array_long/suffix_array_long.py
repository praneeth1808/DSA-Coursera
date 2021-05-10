# python3
import sys

def SortCharacters(n,text):

  CharMap = {"$":0,"A":1,"C":2,"G":3,"T":4}
  count = [0,0,0,0,0]
  order = [-1] * n

  for char in text:
    index = CharMap[char]
    count[index] = count[index] + 1

  count[1] = count[1] + count[0]
  count[2] = count[2] + count[1]
  count[3] = count[3] + count[2]
  count[4] = count[4] + count[3]

  for i in range(n-1,-1,-1):
    char = text[i]
    index = CharMap[char]
    count[index] = count[index] -1
    order[count[index]] = i
  return order

def ComputeCharClasses(n,S,order):
  CLassArr = [-1] * len(S)
  CLassArr[order[0]] = 0

  for i in range(1,n):
    if (S[order[i]] != S[order[i-1]]):
      CLassArr[order[i]] = CLassArr[order[i-1]]+1
    else:
      CLassArr[order[i]] = CLassArr[order[i - 1]]
  return CLassArr


def SortDoubled(n,S,L,order,ClassArr):
  count = [0] * n
  newOrder = [-1] * n

  for i in range(n):
    count[ClassArr[i]] = count[ClassArr[i]] + 1

  for j in range(1,n):
    count[j] = count[j] + count[j-1]
  for i in range(n-1,-1,-1):
    start = (order[i] - L + n) % n
    cl = ClassArr[start]
    count[cl] = count[cl] -1
    newOrder[count[cl]] = start

  return  newOrder


def UpdateClass(order,ClassArr,L):
  n = len(order)
  newClass = [-1] * n
  newClass[order[0]] = 0

  for i in range(1,n):
     cur = order[i]
     prev = order[i-1]
     mid = cur+L
     midPrev = (prev + L) % n
     if ((ClassArr[cur] != ClassArr[prev]) or (ClassArr[mid] != ClassArr[midPrev])):
       newClass[cur] = newClass[prev] + 1
     else:
       newClass[cur] = newClass[prev]

  return newClass

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  n=len(text)
  order = SortCharacters(n,text)
  ClassArr = ComputeCharClasses(n, text, order)

  L = 1
  while L < n:
    order = SortDoubled(n,text,L,order,ClassArr)
    ClassArr = UpdateClass(order,ClassArr,L)
    L = 2*L

  # Implement this function yourself
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str,build_suffix_array(text) )))
