#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 



class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
       
        self.graph.append([u,v,w])
        
    def Dijkstra(self, s):
        output = {}
        for numbers in range(self.V):
            final = g.graph[numbers]
            for i in range(self.V):
                for each in range(len(final)):
                    if final[each] != 0:
                        nextlist = g.graph[each]
                        for d in range(len(nextlist)):
                            if nextlist[d] != 0:
                                if final[d] == 0 or final[d] > final[each] + nextlist[d]:
                                    final[d] = final[each] + nextlist[d]
            self.graph[numbers] = final
        
        for v in range(self.V):
            self.graph[v][v] = 0
            
        for v in range(self.V):
            output[str(v)] = self.graph[s][v]
            
        return output
        
      
        
       
    
    def find(self, p, i): 
        if p[i] == i: 
            return i 
        return self.find(p, p[i]) 
  
  
    def union(self, p, rank, x, y): 
        xroot = self.find(p, x) 
        yroot = self.find(p, y) 
  
        
        if rank[xroot] < rank[yroot]: 
            p[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            p[yroot] = xroot 
  
       
        else : 
            p[yroot] = xroot 
            rank[xroot] = rank[xroot] + 1    

  
   
    def Kruskal(self): 
  
        result =[] 
  
        i = 0 ; e = 0 
  
          
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        p = [] 
        rank = [] 
  
        
        for node in range(self.V): 
            p.append(node) 
            rank.append(0) 
      
        
        while e < self.V -1 : 
  
            
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(p, u) 
            y = self.find(p ,v) 
  
          
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(p, rank, x, y)             
      
        answer = {}
        for u,v,weight  in result: 
            answer[str(u)+'-'+str(v)] = weight
                           
        return answer        
                

