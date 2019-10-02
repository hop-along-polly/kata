import pytest

from .linked_list import (
    LinkedList,
    DoublyLinkedList,
    CircularList
)
from .node import Node
from .exceptions import NodeNotFoundException


########################################
#       Singly Linked List Tests       #
########################################
#1
def test_ll_construct_empty_list():
    subject = LinkedList()
    assert subject == []

#2
def test_ll_add_to_empty_list():
    # arrange
    subject = LinkedList()
    node = Node('a')

    # act
    actual = subject.add(node)

    # assert
    assert actual == 'a'
    assert subject == ['a']

#3
def test_ll_add_to_populated_list():
    # arrange
    subject = LinkedList()

    # setup the nodes to add
    existing_node = Node('existing')
    new_node = Node('new')
    
    # seed the list with a node
    subject.add(existing_node)

    # act
    actual = subject.add(new_node)

    # assert
    assert actual == 'new'
    assert subject == ['existing', 'new']

#4
def test_ll_remove_empty_list():
    # arrange
    subject = LinkedList()
    
    # assert
    assert subject.remove('dne') == None
    assert subject == []

#5
def test_ll_remove_first_item_in_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))

    actual = subject.remove('a')
    # assert
    assert actual == 'a'
    assert subject == []

#6
def test_ll_remove_first_item_in_populated_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    #act
    actual = subject.remove('first')
    
    # assert
    assert actual == 'first'
    assert subject.as_list() == ['second']
    assert subject == ['second']

#7
def test_ll_remove_item_in_middle_of_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    # assert
    assert subject.remove('b') == 'b'
    assert subject == ['a', 'c']

#8
def test_ll_remove_last_item_in_the_list():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))

    # assert
    assert subject.remove('b') == 'b'
    assert subject == ['a']

#9
def test_ll_remove_node_that_appears_multiple_times():
    # arrange
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    # assert
    assert subject.remove('b') == 'b'
    assert subject == ['a', 'b', 'c']


########################################
#       Doubly Linked List Tests       #
########################################
#10
def test_dl_construct_empty_list():
    # arrange
    subject = DoublyLinkedList()
    # assert
    assert subject == []

#11
def test_dl_add_to_empty_list():
    # arrange
    subject = DoublyLinkedList()

    #act
    node = Node('a')
    subject.add(node)

    # assert
    assert subject == ['a']

#12
def test_dl_add_to_populated_list():
    subject = DoublyLinkedList()
    subject.add(Node('existing'))

    #act
    node = Node('new')
    subject.add(node)

    # assert
    assert subject == ['existing', 'new']

#13
def test_dl_remove_empty_list():
    # arrange
    subject = DoublyLinkedList()
    #act
    subject.remove('dne')

    # assert
    assert subject == []

#14
def test_dl_remove_first_item():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    #act
    subject.remove('first')

    # assert
    assert subject == ['second']

#15
def test_dl_remove_last_item():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    #act
    subject.remove('second')

    # assert
    assert subject.as_list() == ['first']
    assert subject == ['first']

#16
def test_dl_remove_item_in_middle_of_list():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))
    subject.add(Node('third'))

    #act
    subject.remove('second')

    # assert
    assert subject == ['first', 'third']

#17
def test_dl_remove_node_that_appears_multiple_times():
    # arrange
    subject = DoublyLinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))
    subject.add(Node('b'))

    #act
    subject.remove('b')

    # assert
    assert subject == ['a', 'c', 'b']

########################################
#     Circularly Linked List Tests     #
########################################

#18
def test_cl_construct_empty_list():
    # arrange
    subject = CircularList()
    # assert
    assert subject == []

#19
def test_cl_add_to_empty_list():
    # arrange
    subject = CircularList()

    #act
    actual = subject.add(Node('a'))

    # assert
    assert actual.value == 'a'
    assert subject == ['a']

#20
def test_cl_add_to_populated_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))

    #act
    actual = subject.add(Node('b'))

    # assert
    assert actual.value == 'b'
    assert subject == ['a', 'b']

#21
def test_cl_add_to_list_of_2_plus():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    
    #act
    actual = subject.add(Node('c'))

    # assert
    assert actual.value == 'c'
    assert subject.as_list() == ['a', 'b', 'c']
    assert subject == ['a', 'b', 'c']

#22
def test_cl_remove_empty_list():
    # arrange
    subject = CircularList()

    # assert
    assert subject.remove('dne') is None

#23
def test_cl_remove_only_item():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))

    #act
    actual = subject.remove('a')

    # assert
    assert actual.value == 'a'
    assert subject == []

#24
def test_cl_remove_first_item_in_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))

    #act
    actual = subject.remove('a')

    # assert
    assert actual.value == 'a'
    assert subject == ['b']

#25
def test_cl_remove_last_item_in_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))

    #act
    actual = subject.remove('b')

    # assert
    assert actual.value == 'b'
    assert subject == ['a']

#26
def test_cl_remove_item_from_middle_of_list():
    # arrange
    subject = CircularList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))
    subject.add(Node('d'))
    subject.add(Node('e'))
    subject.add(Node('f'))

    #act
    actual = subject.remove('d')

    # assert
    assert actual.value == 'd'
    assert subject == ['a', 'b', 'c', 'e', 'f']
