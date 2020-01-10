#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        
        if root is not None:
            
            if val == root.val:
                return root
            if val < root.val:
                return self.searchBST(root.left, val)
            if val > root.val:
                return self.searchBST(root.right, val)
            else:
                return None

