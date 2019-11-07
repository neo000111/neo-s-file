#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Solution(object):
    
    def MergeSort(self, arr):
            
            length = len(arr)
            if length > 1:
                mid = len(arr) // 2 #取整數
                L = arr[0:mid] #取得左半邊的資料
                R = arr[mid:len(arr)] #取得右半邊的資料
                self.MergeSort(L) #將左右兩邊丟回繼續分割
                self.MergeSort(R)
                return Merge(arr,L,R) #丟到Merge做比較與合併
    def Merge(arr,L,R):
        
        a = arr
        lindex = rindex = aindex = 0 #取得左右及原陣列的索引
        while lindex < len(L) and rindex < len(R): 
            if L[lindex] < R[rindex]: #左右開始比較
                a[aindex] = L[lindex] #左邊較小則把左邊的值賦予回原陣列做替換
                lindex += 1 #左邊索引往右走
            else:
                a[aindex] = R[rindex] #反之就將右邊的值賦予回原陣列
                rindex += 1
            aindex += 1 #原陣列往右
        while lindex < len(L):
            a[aindex] = L[lindex]
            lindex += 1
            aindex += 1
        while rindex < len(R):
            a[aindex] = R[rindex]
            rindex += 1
            aindex += 1
        return arr
    
        

