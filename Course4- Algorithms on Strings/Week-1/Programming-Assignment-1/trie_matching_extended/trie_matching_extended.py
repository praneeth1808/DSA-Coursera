# python3
import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4


def build_trie(patterns):
    tree = dict()
    # write your code here
    tree[0] = dict()
    rank = 1
    for pattern in patterns:
        currentNode = 0
        for i in pattern:
            currentSymbol = i
            found = 0
            for j in tree[currentNode].keys():
                if currentSymbol == j:
                    found = 1
                    currentNode = tree[currentNode][j]
                    break
            if found == 0:
                tree[currentNode][currentSymbol] = rank
                tree[rank] = dict()
                currentNode = rank
                rank += 1
        tree[currentNode]["$"]=-1
    return tree

def PrefixTrieMatching(text,trie):
    i=0
    text+="$"
    symbol=text[i]
    v=0
    while True:
        if("$" in trie[v].keys()):
            return True
        elif(symbol in trie[v].keys()):
            i+=1
            v = trie[v][symbol]
            symbol=text[i]
        else:
            return False


def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    i = 0
    # write your code here
    while len(text) != 0:
        if (PrefixTrieMatching(text, trie)):
            result.append(i)
        text = text[1:]
        i += 1
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
