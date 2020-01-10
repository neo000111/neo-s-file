#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution:
    def sortArray(self, nums):
        s = []
        b = []
        k = []
        if len(nums) <= 1:
            return nums
        else:
            key = nums[0]
            for i in nums:
                if i < key:
                    s.append(i)
                elif i > key:
                    b.append(i)
                else:
                    k.append(i)
        s = self.sortArray(s)
        b = self.sortArray(b)
        return s + k + b

