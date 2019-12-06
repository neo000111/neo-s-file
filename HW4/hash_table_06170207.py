#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Crypto.Hash import MD5
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def ckey(self, text):
        h = MD5.new()
        h.update(text.encode("utf-8"))
        n = int(h.hexdigest(),16)
        return n
    
    def index(self, key):
        n = self.ckey(key)
        return n % self.capacity
        
    def add(self, key):
        if self.contains(key) is False:
            
            n = self.ckey(key)
            a = self.index(key)
            c = self.data[a]
            if c is None:
                self.data[a] = ListNode(n)
            else:
                while cur:
                    if c.val == n:
                        return
                    if c.next is None:
                        c.next = ListNode(n)
                        return 
                    else:
                        c = c.next
                return
        else:
            pass
        
    def remove(self, key):
        n = self.ckey(key)
        a = self.index(key)
        c = self.data[a]
        if self.contains(key) is True:
            if c.val == n:
                self.data[a] = c.next
            while c.next:
                if c.next.val == n:
                    c.next = c.next.next
                    return
                c = c.next
            return
                      
    def contains(self, key):
        n = self.ckey(key)
        a = self.index(key)
        c = self.data[a]
        while c :
            if c.val == n:
                return True
            c = c.next
        return False

