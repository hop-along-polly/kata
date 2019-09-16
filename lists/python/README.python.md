# Python Linked Lists
## Getting started
You will be implementing 3 classes located in the `linked_list.py` module. A `Node` class
has been provided that will suitable for the 3 lists you will be implementing. You are
free to define your own `Node` but the tests do expect the predefined structure. Each of
the lists inherit from a base `List` class which provides a `__eq__` method that helps in
the unit test assertions. If you choose to break that inheritance you'll need to provide a
similar implementation to `List.__eq__`.
_NOTE: the `Node` class defines a prev attribute that can be ignored for the SingluarLinkedList._

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
