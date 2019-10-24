# 堆積排序法(Heap Sort)

## 介紹

堆積排序法就是把節點中最大或最小的數值放在根節點(root)，堆積排序法的目的是為了減少選擇排序法的比對次數。它以二元樹為基底，使每一筆資料的比對次數，不會大於 O(n log(n)) ，並且它不需多餘記憶的空間，也沒有使用遞迴函數，其時間複雜度為O(n log(n))，然而其缺點是每次排序都必須重建heap，增加O(N)時間複雜度。它利用二元堆積樹來完成排序，下面簡單介紹一下二元堆積樹。

## 二元堆積樹(Binary Heap)

有兩項基本特徵:

### 特徵一 : 它是一個完整二元樹。其優點是方便尋找 parent-child 之關係，以index(i)的node為例:

其left child必定位在index(2i)；
其right child必定位在index(2i+1)；
其parent必定位在index(⌊i/2⌋)。

<img src='https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Sorting%20series/ComparisonSort_fig/HeapSort/f1.png?raw=true'>
圖片來源:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

### 特徵二 : 若將位於index(i)的節點視為堆積樹的根節點(root)，可將二元堆積樹分為兩類 :

Max Heap : 在每一個堆積樹中，root之「數值」要比兩個child之「數值」還要大。

Min Heap : 在每一個堆積樹中，root之「數值」要比兩個child之「數值」還要小。


<img src='https://github.com/alrightchiu/SecondRound/blob/master/content/Algorithms%20and%20Data%20Structures/Sorting%20series/ComparisonSort_fig/HeapSort/f2.png?raw=true'>
圖片來源:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

特別注意：在同一個堆積樹中，leftchild(index(2i))與rightchild(index(2i+1))的「數值」大小順序不重要，只要和root(index(i))比較即可。

要滿足Binary Heap特有的「parent-child」之關係，只要讓矩陣中index(0)的位置閒置，從index(1)開始存放資料，即可使用矩陣(array)來表示Binary Heap。

參考資料:(http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)

