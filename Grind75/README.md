# 14 Patterns to Ace Any Coding Interview Question

## 1. Sliding Window
- `Used to perform operation on a specific window size pf array or linked list`
    - `i.e. finding longest subarray containing all 1s`
- Start from first element, shift right by one element and adjust sthe length of window

<p align="center">
  <img src="media\Sliding_Window.png"/>
</p>

### How to identify
- `Problem input is linear data structure such as a linked list, array or string`
- `Asked to find longest/shortest substring, sub array or a desired value`
### Featured Problems
- Maximum size of subarray of size 'K' (easy)
- Longest substring with 'K' disinct characters (medium)
- String anagrams (hard)

## 2. Two Pointers or Iterators
- `Useful when searing pairs in a sorted array or linked list`
    - `i.e. when you have to compare each element of an array to it's other elements`
- Iterate through data structure in tandem until one or both pointers hit a certain condition.

<p align="center">
  <img src="media\Two_Pointers.png"/>
</p>

### How to identify
- `Problem will feature sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints`
- `The set of elements in the array is a pair, a triplet or even a subarray`
### Featured Problems
    - Squaring a sorted array (easy)
- Triplets that sum to zero (medium)
- Comparing strings that contain backspaces (medium)

## 3. Fast and Slow Pointers 
- `Useful when dealing with cyclic linked lists or arrays`
    - The fast and slow pointers are bound to meet
- The algorithm uses two points which move through the array (or sequence/linked list) at different speeds.


<p align="center">
  <img src="media\Fast_and_Slow.png"/>
</p>

### How to identify
- `The problem will deal with a loop in a linked list or array`
- `When you need to know the position of a certain element or the overall length of the linked list`
### When to use over Two Pointer?
- Singly linked list when you can't move backwards
    - i.e. Trying to determine wheter list is palindrome
### Featured Problems
- Linked list cycle (easy)
- Palindrome linked list (medium)
- Cycle in Circular Array (hard)

## 4. Merge Intervals
- `When you either need to find overlapping values or merge intervals if they overlap`
- `Efficient technique to deal with overlapping Intervals`
- Six different ways that the two intervals can relate to each other

<p align="center">
  <img src="media\Merge_Intervals.png"/>
</p>

### How to identify
- `If you're asked to produce a list with only mutually exclusive intervals`
- `If you hear the term "overlapping intervals"`
### Featured Problems    
- Invervals Intersection (medium)
- Maximum CPU Load (hard)

## 5. Cyclic Sort
- `An approach to deal with problems involving arrays containing numbers in a given range.`
- iterates over array one number at a time and if the current number we are iterating is not at the correct index, swap it with the number at it's correct index

<p align="center">
  <img src="media\Cyclic_Sort_1.png"/>
  <img src="media\Cyclic_Sort_2.png"/>
</p>

### How to identify
- `Problems involving sorted array with numbers in a given range`
- `If the problem asks you to find the missing/duplicate/smallest number in a sorted array`
### Featured Problems
- Find the missing number (easy)
- Find the smallest missing positive number (medium)

## 6. In-place reversal of linked list
- `Reverse the links between a set of nodes in a linked list using the existing node objects and without using extra memory.`
- The pattern reverses one node at a time starting with one variable (current) point to the head of the linked list, and one variable (previous) will point to the previous node that we have processed. We will reverse the current node by pointing it to previous before moving on to the next node. We will also  update the variable "previous" to always point to the previous node we have processed

<p align="center">
  <img src="media\In-place_reversal_of_linked_list.png"/>
</p>

### How to Identify
- `When asked to reverse a linked list without using extra memory`
### Featured Problems
- Reverse a Sub-list (medium)
- Reverse every K-element Sub-list (medium)

## 7. Tree BFS
- `Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach.`
- Based on Breadth First Search (BFS), uses a queue to keep track of all nodes of a level before jumping to next.
- Works by pushing root node to the queue and then continually iterating until the queue is empty
    - We remove the node at the head of the queue and visit that node and append it's children to the queue (left first)

<p align="center">
  <img src="media\Tree_BFS.png">
</p>

### How to Identify
-   `When asked to traverse a tree in a level-by-level fashion (or level order traversal)`
### Featured Problems
- Binary Tree Level Order Traversal (easy)
- Zigzag Traversal (medium)

## 8. Tree DFS
- Based on the Depth First Search (DFS) technique
- Use a recursion (or a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing
- Start at root of tree, if node is not a leaf, we do two things
    1. Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order).

    <p align="center">
      <img src="media\Tree_Traversal_Order.png">
    </p>

    2. Make two recursive calls for both the children of the current node to process them.
### How to identify
- `When asked to traverse a tree with in-order, preorder or postorder DFS`
- `If the problem requires searching for something where the node is closer to a leaf`
### Featured Problems
- Sum of Path Numbers (medium)
- All Paths for a Sum (medium)

## 9. Two Heaps
- `Useful for problems when we are given a set of elements such that we can divide them into two parts and we are interested in knowing the smallest element in one part and the biggest element in the other part`.
- Uses two heaps:
    1. Min Heap to find smallest element
    2. Max Heap to find largest element

<p align="center">
  <img src="media\MinHeapAndMaxHeap1.png">
</p>

- Works by:
    1. Storing first half of numbers in a Max Heap (if we want to find the largest number in first half)
    2. Store second half of numbers in a Min Heap (if we want to find the smallest number in second half)
    3. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

### How to identify
- `Useful in situations like Priority Queue, Scheduling`
- `If the problem states that you need to find the smallest/largest/median elements of a set`
- `Sometimes, useful in problems featuring a binary tree data structure`
### Featured Problems
- Find the Median of a Number Stream (medium)

# 10. Subsets
- `Deals with problems involve dealing with Permutations (like given a String, find all combinations of the characters) and Combinations of a given set of elements.` 
- The pattern Subsets describes an efficient Breadth First Search (BFS) approach to handle all these problems.

- The pattern looks like this: Given a set of [1, 2, 3]:
  1. Start with an empty set: [[]]
  2. For each element in the set, add the element to the existing set to create 
    - i.e. First number(1): new subsets: [[], [1]];
    - Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
    - Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].

<p align="center">
  <img src="media\subsets_example.png">
</p>

## How to Identify
-  `Probelms where you need to find combinations or permutations of a given set`
## Featured Problems
- Subsets With Duplicates (easy)
- String Permutations by changing case (medium)

# 11. Modified binary search
- `When given a sorted array, linked list, or matrix, and are asked to find a certain element`
- The pattern looks for an ascending order set (numbers in increasing order, that is, from smallest to largest)
  1. Find the middle, start and end. 
      - middle = (start + end)/2 may produce an integer overflow
      - middle = start + (end-start)/2 is recommended
  2. If 'key' is equal to number at index middle then return middle
  3. If ‘key’ isn’t equal to the index middle:
  4. Check if key < arr[middle]. If it is reduce your search to end = middle — 1
  5. Check if key > arr[middle]. If it is reduce your search to end = middle + 1

<p align="center">
  <img src="media\Modified_Binary_Search.png">
</p>

## Featured Problems
- Order-agnostic Binary Search (easy)
- Search in a Sorted Infinite Array (medium)

# 12. Top K Elements
- `Any problems that ask us to find the top/smallest/frequent 'K' elemnts among a given set`
- The best data structure to keep track of ‘K’ elements is Heap.
- It works as follows:
  1. Insert ‘K’ elements into the min-heap or max-heap based on the problem.
  2. Iterate through the remaining numbers and if you find one that is larger (or smaller, depends on problem) than what you have in the heap, then remove that number and insert the larger (or smaller) one.

<p align="center">
  <img src="media\Top_K_Elements.png">
</p>



  ~~~
  import heapq
  import numpy as np

  def maxHeap(array): #inverting all numbers in the array to essentially perform a maxHeap
      array = np.array(array)
      array = -array
      array = array.tolist()
      heapq.heapify(array)
      array = np.array(array)
      array = -array
      array = array.tolist()
      return array

  def getTopK(a, k):
    temp = a[:k]
    for i in range(k, len(a)):
        if temp[0] < a[i]:
            heapq.heappop(temp)
            heapq.heappush(temp, a[i])
    return temp

  def getSmallestK(a, k):
    a = maxHeap(a)
    temp = a[:k]
    for i in range(k, len(a)):
        if temp[0] > a[i]:
            heapq.heappop(temp)
            heapq.heappush(temp, a[i])
            temp = maxHeap(temp)
    return temp

  a= np.random.randint(100, size=10)
  a = a.tolist()
  smallest = getSmallestK(a,5)
  largest = getTopK(a, 5)
  print(smallest)
  print(largest)
  ~~~

## How to identify
- `If you’re asked to find the top/smallest/frequent ‘K’ elements of a given set`
- `If you’re asked to sort an array to find an exact element`

## Featured Problems
- Top ‘K’ Numbers (easy)
- Top ‘K’ Frequent Numbers (medium)

# 13. K-way Merge
- `Problems involving a set of sorted arrays`
- Use a Heap to efficiently perform a sorted traversal of all the elements of all arrays
  1. Push the smallest element of each array in a Min Heap to get the overall minimum
  2. Push the next element from the same array to the heap
  3. Repeat this process to make a sorted traversal of all elements

- The illustration below follows this pattern:
    1. Insert the first element of each array in a Min Heap.
    2. After this, take out the smallest (top) element from the heap and add it to the merged list.
    3. After removing the smallest element from the heap, insert the next element of the same list into the heap.
    4. Repeat steps 2 and 3 to populate the merged list in sorted order.
    
<p align="center">
  <img src="media\K_Way_Merge.png">
</p>

## How to identify the K-way Merge pattern:
- `The problem will feature sorted arrays, lists, or a matrix`
- `If the problem asks you to merge sorted lists, find the smallest element in a sorted list.`

## Problems featuring the K-way Merge pattern:
- Merge K Sorted Lists (medium)
- K Pairs with Largest Sums (Hard)

# 14. Topological Sort
- `Used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.`
- The pattern works like this:
  1. Initialization
      <ol type="a">
        <li>Store the graph in adjacency lists by using a HashMap</li>
        <li>To find all sources, use a HashMap to keep the count of in-degrees (in-degree is the number of connections that point inward at a vertex. Out-degree is the number of connections that originate at a vertex and point outward to other vertices.)</li>
      </ol>
  2. Build the graph and find in-degrees of all vertices
      <ol type="a">
        <li>Build the graph from the input and populate the in-degrees HashMap.</li>
        <li>To find all sources, use a HashMap to keep the count of in-degrees</li>
      </ol>
  3. Find all sources
      <ol type="a">
        <li>All vertices with ‘0’ in-degrees will be sources and are stored in a Queue.</li>
      </ol>
  4. Sort
      <ol type="a">
        <li>For each source, do the following things:</li>
        <ol type = "I">
          <li>Add it to the sorted list.</li>
          <li>Get all of its children from the graph.</li>
          <li>Decrement the in-degree of each child by 1.</li>
          <li>If a child’s in-degree becomes ‘0’, add it to the sources Queue.</li>
        </ol>
        <li>Repeat (a), until the source Queue is empty.</li>
      </ol>

<p align="center">
  <img src="media\topological-sorting.png">
</p>

## How to Identify
- `The problem will deal with graphs that have no directed cycles`
- `If you’re asked to update all objects in a sorted order`
- `If you have a class of objects that follow a particular order`

## Featured Problems
- Task scheduling (medium)
- Minimum height of a tree (hard)