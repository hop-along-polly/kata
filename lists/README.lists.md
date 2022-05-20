# Linked Lists
Linked lists are one of the simplest data structures and act very similarly to an array
or list in Python. The advantage of a linked list is that it does not use contiguous 
memory to store objects. This saves you from having to pre-allocate all the memory the
data structure needs and from reallocating memory as the amount of data grows and shrinks.

The way linked lists achieve linear time operations is by storing nodes which represent
the actual stored value and a pointer `next` to the memory location where the next node
is located. There is a special pointer called `HEAD` that always points to the most
recently added node. The final nodes `next` pointer points to a null value indicating
you have reached the end of the linked list. 

## Interface
The foundational operations for a Linked List are `add`, `remove`, and `find`, any other
operations is a combination of these operations. For example `add_last` is a combination
of `find` and `add`.

The Following operations would create a linked list that would look like this
```python
add('python')
add('rust')
add('node.js')
add('C#')
remove('rust')

#   HEAD
#    |
#    V
#+------------+    +-------------+    +--------+
#| Python | o----->| node.js | o----->| C# | o-----> NULL
#+------------+    +-------------+    +--------+
```

## Algorithmic Complexity
 - `add`: O(n)
 - `remove`: O(n)
 - `find`: O(n)
