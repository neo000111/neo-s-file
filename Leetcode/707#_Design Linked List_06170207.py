#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next



class MyLinkedList:

    def __init__(self):
        self.head = None
        
       
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
          
        cur = self.head
        for i in range(index):
            if cur:
                cur = cur.next
            else:
                break
        return cur.val if cur else -1
        
        
        
         
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head = Node(val=val, next=None)
        else: 
            tmp = self.head
            self.head = Node(val=val, next=tmp)
        
        
      
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            
            self.head = Node(val=val, next=None)
        else: 
            head = self.head
            while head.next:
                head = head.next
            head.next = Node(val=val, next=None)
       
    def addAtIndex(self, index, val) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        head = self.head
        if head:
            for i in range(index-1):
                if head.next:
                    head = head.next
                else:
                    return 
            tmp = Node(val=val, next=head.next)
            head.next = tmp
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self.head
        if head:
            if index == 0:
                self.head = self.head.next
            else:
                for i in range(index-1):
                    if head.next:
                        head = head.next
                    else:
                        return
                if head.next:
                    head.next = head.next.next  



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

