#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
    
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = Node(x, next=None)
        else: 
            tmp = self.head
            self.head = Node(x, next=tmp)
            

    def pop(self) -> None:
        if self.isempty():
            return None
        else:
            top = self.head
            self.head = self.head.next
            top.next = None
            return top.val
        
        

    def top(self) -> int:
        if self.isempty():
            return None
        else:
            return self.head.val
        

    def getMin(self) -> int:
        node = self.head
        if self.isempty():
            return None
        Min = node.val
        while node:
            if node.val < Min:
                Min = node.val
            node = node.next
        return Min

