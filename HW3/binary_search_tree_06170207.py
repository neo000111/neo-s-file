#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """


class Solution(object):
    
    def show(self, root):
        if root is not None:
            self.showtree(root)
    def showtree(self, cur):
        if cur is not None:
            self.showtree(cur.left)
            print(str(cur.val), end=' ')
            self.showtree(cur.right)
            

            
    
    def insert(self, root, val):
        
    
        if root is None:
            return TreeNode(val)
        else:
            if val <= root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                    
                else:
                    self.insert(root.left, val)
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    
                else:
                    self.insert(root.right, val)
        return root
    def search(self, root, target):
        
        if root is not None:
            if target == root.val:
                return root
            if target < root.val:
                return self.search(root.left, target)
            if target > root.val:
                return self.search(root.right, target)
       
        else:
            return None
    def delete(self, root, target):   
        while self.search(root, target):
            self.remove(root, target)
        return root
    
    def remove(self, root, val):
        if not root: 
            return None
        if root.val == val:
            if not root.left and not root.right: 
                return None
            if not root.left: 
                return root.right
            if not root.right: 
                return root.left
            left = root.left
            right = root.right
            
            while right.left: 
                right = right.left
            right.left = left
            return right
        if val > root.val: 
            root.right = self.remove(root.right, val)
        else: 
            root.left = self.remove(root.left, val)
            
        return root
            
    def modify(self, root, target, new_val):
        while self.search(root, target):
            self.remove(root, target)
            self.insert(root, new_val)
        
        return root

