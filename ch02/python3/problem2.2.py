import linkedList

def kthMember(lList, k):
  temp = []
  n = lList.head
  
  while (n != None):
    temp.append(n.data)
    n = n.next
  
  return temp[-k]

myHeadNode = linkedList.Node(1)
myHeadNode.appendToTail(2)
myHeadNode.appendToTail(1)
myHeadNode.appendToTail(3)
myHeadNode.appendToTail(2)
myHeadNode.appendToTail(4)
myHeadNode.appendToTail(3)

myLinkedList = linkedList.LinkedList(myHeadNode)
print('--- 連結リスト L ---')
myLinkedList.printLinkedList()

print('Lの後ろから3番目の要素は' + str(kthMember(myLinkedList, 3)) + 'です。')
