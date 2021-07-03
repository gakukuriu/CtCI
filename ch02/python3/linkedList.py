class Node:
  next = None
  data = 0

  def __init__(self, n):
    self.data = n

  def appendToTail(self, d):
    end = Node(d)
    n = self
    while (n.next != None):
      n = n.next
    n.next = end


class LinkedList:
  head = Node

  def __init__(self, node):
    self.head = node

  def printLinkedList(self):
    n = self.head
    temp = []
    while (n != None):
      temp.append(n.data)
      n = n.next
    print(' -> '.join(map(lambda x: str(x), temp)))


def deleteNode(lList, d):
  n = lList.head

  if (n.data == d):
    return LinkedList(n.next)

  while (n.next != None):
    if (n.next.data == d):
      n.next = n.next.next
      return lList
    n = n.next

  return lList
