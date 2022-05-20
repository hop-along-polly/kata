# Python Linked Lists
## Getting started
You will be implementing 3 classes located in the `linked_list.py` module. A `Node` class
has been provided that will suitable for the 3 lists you will be implementing. You are
free to define your own `Node` but the tests do expect the predefined structure. Each of
the lists inherit from a base `List` class which provides a `__eq__` method that helps in
the unit test assertions. If you choose to break that inheritance you'll need to provide a
similar implementation to `List.__eq__`.
__NOTE: the `Node` class defines a prev attribute that can be ignored for the SingluarLinkedList.__

## Running the Tests
To run the tests for linked lists use the following command
```bash
pytest -x lists/  # -x stops the test suite on the first failure
```
_NOTE: using `-x` is recommended so you can follow a flow similar to test driven development._

You can filter out specific tests i.e. just the DoublyLinkedList tests using the `-k` flag.
```bash
pytest -x -k test_dl lists/
```

You can use the following filters to run tests for the specific type of lists
  - LinkedList: `-k test_ll`
  - DoubleLinkedList: `-k test_dl`
  - CircularlyLinkedList: `-k test_cl`


## Interview Question Warm-Up
Most technical interviews require a developer to implement a function with some
constraints on the algorithmic and space complexity. To help prepare for interviews this
section talks about one such algorithm that can be solved using a LinkedList to implement
a Stack. A Stack if a First-In-Last-Out `(FILO)` data structure. So the first thing
`pushed` onto the Stack is the last thing to be `pop`ed off the Stack. To truly support
this you will need to implement a `push` and `pop` function.

`push` will take a node just like add but will always add it to the front of the list.
`pop` will always remove the node that HEAD points to.

Your challenge should you choose to accept it is to implement a function that takes in a
string and determines if all of the `(`, `{`, and `[` have a corresponding closing `]`,
`}`, `)`.

For example
```python
example = '()[]{}';
is_valid(example)
# returns True

example = '('
is_valid(example)
# returns False
```

To help you get started you should push when you encounter a `(`, `{`, `[` and pop when
you encounter a `]` `}`, and `)`.
