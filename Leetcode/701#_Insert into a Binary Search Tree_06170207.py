#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        
        if root is None:
            return TreeNode(val)
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    
                else:
                    self.insertIntoBST(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    
                else:
                    self.insertIntoBST(root.right, val)
        return root

