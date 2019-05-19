import pytest

from .linked_list import LinkedList
from .node import Node
from .exceptions import NodeNotFoundException


def test_ll_construct_empty_list():
    subject = LinkedList()
    assert subject == []


def test_ll_add_to_empty_list():
    # arrange
    subject = LinkedList()
    node = Node('a')

    # act
    actual = subject.add(node)

    # assert
    assert actual == 'a'
    assert subject == ['a']


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


def test_ll_remove_empty_list():
    subject = LinkedList()

    assert subject.remove('dne') == None
    assert subject == []


def test_ll_remove_first_item_in_list():
    subject = LinkedList()
    subject.add(Node('a'))

    actual = subject.remove('a')
    assert actual == 'a'
    assert subject == []


def test_ll_remove_first_item_in_populated_list():
    subject = LinkedList()
    subject.add(Node('first'))
    subject.add(Node('second'))

    actual = subject.remove('first')
    assert actual == 'first'
    assert subject.as_list() == ['second']
    assert subject == ['second']


def test_ll_remove_item_in_middle_of_list():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    assert subject.remove('b') == 'b'
    assert subject == ['a', 'c']


def test_ll_remove_last_item_in_the_list():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))

    assert subject.remove('b') == 'b'
    assert subject == ['a']


def test_ll_remove_node_that_appears_multiple_times():
    subject = LinkedList()
    subject.add(Node('a'))
    subject.add(Node('b'))
    subject.add(Node('b'))
    subject.add(Node('c'))

    assert subject.remove('b') == 'b'
    assert subject == ['a', 'b', 'c']
