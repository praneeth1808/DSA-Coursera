# python3
import sys

def ComputePrefixFunction(text):
  length = len(text)
  s=[0]*length
  border = 0
  for i in range(1,length):
    while ( border>0) and (text[i] != text[border]):
      border = s[border - 1]
    if (text[i] == text[border]):
      border +=1
    else:
      border = 0
    s[i] = border
  return s


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  s = ComputePrefixFunction(pattern+"$"+text)
  result = []
  len_pattern = len(pattern)
  for i in range(len_pattern+1,len(s)):
    if s[i] == len_pattern:
      result.append(i-2*len_pattern)
  # Implement this function yourself
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

