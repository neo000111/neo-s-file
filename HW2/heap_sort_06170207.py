#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def heap_sort(self, arr):
        length = len(arr)
        leastparent = length // 2 - 1
        for i in range(leastparent, -1, -1):
            self.maxheap(arr, i, length)
        print("maxheap", arr)
        for i in range(length-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.maxheap(arr, 0, i)
        return arr
    def maxheap(self, arr, i, length):
        root = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < length and arr[left] > arr[root]:
            root = left
        
        if right < length and arr[right] > arr[root]:
            root = right
    
        if root != i:
            arr[root], arr[i] = arr[i], arr[root]
            self.maxheap(arr, root, length)

