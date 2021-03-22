#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  print(tree)
  return True

class BinaryTree:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def isBinaryTree(self,i=0,maxi=2147483648,mini=-2147483648):
    if i == -1:
      return True
    if self.key[i]<mini or self.key[i]>maxi:
      return False

    return  self.isBinaryTree(self.left[i],self.key[i]-1,mini) and self.isBinaryTree(self.right[i],maxi,self.key[i]+1)


def main():
  tree = BinaryTree()
  tree.read()
  if tree.n == 0:
    print("CORRECT")
    return
  if tree.isBinaryTree():
    print("CORRECT")
  else:
    print("INCORRECT")


threading.Thread(target=main).start()
