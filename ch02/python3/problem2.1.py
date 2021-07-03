import linkedList

def deleteDuplication(lList):
  temp = []
  n = lList.head

  while (n.next != None):
    temp.append(n.data)
    if (n.next.data in temp):
      while (n.next != None and n.next.data in temp):
        n.next = n.next.next
      if (n.next == None):
        break
      n = n.next
    else:
      n = n.next
  return lList
  

myHeadNode = linkedList.Node(1)
myHeadNode.appendToTail(2)
myHeadNode.appendToTail(1)
myHeadNode.appendToTail(3)
myHeadNode.appendToTail(2)
myHeadNode.appendToTail(4)
myHeadNode.appendToTail(3)

myLinkedList = linkedList.LinkedList(myHeadNode)
print('--- 現在の連結リスト ---')
myLinkedList.printLinkedList()

print('--- 重複要素を削除した後の連結リスト ---')
deleteDuplication(myLinkedList).printLinkedList()





