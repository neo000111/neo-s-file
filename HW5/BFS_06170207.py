#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 
  


class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 
        

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s): 
        visisted = [] 
        alist = [s]   
        visisted.append(s) 
        while len(alist) > 0: 
            u = alist.pop(0)  
            for n in self.graph[u]: 
                if n not in visisted: 
                    visisted.append(n) 
                    alist.append(n)    
        return visisted 
    
    def DFS(self, s):
        stack, visited = [s], []  
        while len(stack) > 0: 
            u = stack.pop(-1) 
            if u not in visited: 
                visited.append(u)
            
            for n in self.graph[u]: 
                if n not in visited: 
                    if n not in stack:
                        stack.append(n)
                    
        return visited

