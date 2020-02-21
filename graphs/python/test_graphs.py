import pytest
from .graph import Graph, NodeDoesNotExistException


def test_graph_node_construct_without_neighbors():
    subject = Graph.Node('A', 1337)

    assert subject.id == 'A'
    assert subject.weight == 1337
    assert subject.neighbors == []


def test_graph_node_construct_with_neighbors():
    neighbor = Graph.Node('Rodgers', 1347)

    subject = Graph.Node('A', 1337, neighbors=[neighbor])

    assert subject.id == 'A'
    assert subject.weight == 1337
    assert subject.neighbors == [neighbor]


def test_graph_node_remove_neighbor_from_graph_node():
    neighbor = Graph.Node('Rodgers', 1337)
    subject = Graph.Node('A', 1337, neighbors=[neighbor])

    subject.remove_neighbor('Rodgers')
    assert subject.neighbors == []


def test_graph_node_remove_neighbor_that_doesnt_exist():
    neighbor = Graph.Node('Rodgers', 1337)
    subject = Graph.Node('A', 1337, neighbors=[neighbor])

    actual = subject.remove_neighbor('who dis')
    assert actual is None


def test_construction_empty_graph():
    subject = Graph()
    assert subject.nodes == []


def test_graph_add_first_node():
    subject = Graph()
    actual = subject.add('A', 1)

    assert subject.empty is False
    assert subject.nodes == [actual]


def test_graph_add_adjacent_nodes():
    subject = Graph()
    first = subject.add('A', 1337)
    second = subject.add('B', 1347, neighbors=['A'])

    assert subject.empty is False
    assert subject.nodes == [first, second]
    assert first.neighbors == [second]
    assert second.neighbors == [first]


def test_graph_add_non_adjacent_nodes():
    subject = Graph()
    first = subject.add('A', 1337)
    second = subject.add('B', 1347)

    assert subject.empty is False
    assert subject.nodes == [first, second]
    assert first.neighbors == []
    assert second.neighbors == []


def test_graph_add_third_node_only_adjacent_to_one_existing_node():
    subject = Graph()
    first = subject.add('A', 1337)
    second = subject.add('B', 1347, neighbors=['A'])
    third = subject.add('C', 12, neighbors=['A'])

    assert subject.empty is False
    assert subject.nodes == [first, second, third]
    assert first.neighbors == [second, third]
    assert second.neighbors == [first]
    assert third.neighbors == [first]


def test_graph_add_node_with_duplicate_id():
    subject = Graph()
    first = subject.add('A', 1337)
    second = subject.add('A', 1337)

    assert first == second


def test_graph_add_node_with_neighbor_that_does_not_exist():
    subject = Graph()
    with pytest.raises(KeyError):
        first = subject.add('A', 1337, neighbors=['dne'])


def test_remove_node_from_empty_graph():
    subject = Graph()
    removed = subject.remove('dne')

    assert removed is True
    assert subject.nodes == []


def test_remove_only_node_from_graph():
    subject = Graph()
    node_a = subject.add('A', 12)

    actual = subject.remove('A')
    assert actual == node_a
    assert subject.empty
    assert subject.nodes == []


def test_remove_node_w_neighbors_from_graph():
    subject = Graph()
    node_a = subject.add('A', 1337)
    node_b = subject.add('B', 1337, neighbors=['A'])

    actual = subject.remove('B')
    assert actual == node_b
    assert subject.nodes == [node_a]
    assert subject.nodes[0].neighbors == []


def test_graph_remove_node_in_cycle_from_graph():
    subject = Graph()
    node_a = subject.add('A', 12)
    node_b = subject.add('B', 2, neighbors=['A'])
    node_c = subject.add('C', 7, neighbors=['A', 'B'])

    actual = subject.remove('B')
    assert actual == node_b
    assert subject.nodes == [node_a, node_c]
    assert subject.nodes[0].neighbors == [node_c]
    assert subject.nodes[1].neighbors == [node_a]


def test_djisktra_on_empty_graph():
    """
    This also covers the case where the node does not exist
    """
    subject = Graph()

    with pytest.raises(NodeDoesNotExistException):
        actual = subject.djikstra('dne')


def test_djikstra_graph_has_a_single_node():
    subject = Graph()
    subject.add('A', 13)

    actual = subject.djikstra('A')
    assert actual == { 'A': 0 }


def test_djikstra_with_only_adjacent_nodes():
    subject = Graph()
    node_a = subject.add('A', 1337)
    node_b = subject.add('B', 1347, neighbors=['A'])

    actual = subject.djikstra('A')
    assert actual == { 'A': 0, 'B': 1347 }


def test_djikstra_where_graph_has_unreachable_node():
    subject = Graph()
    subject.add('A', 1337)
    subject.add('B', 1347)

    actual = subject.djikstra('A')
    actual == { 'A': 0, 'B': -1 }


def test_djikstra_where_graph_has_multiple_nodes():
    subject = Graph()
    subject.add('A', 1)
    subject.add('B', 2, neighbors='A')
    subject.add('C', 7, neighbors='B')

    actual = subject.djikstra('A')
    assert actual == { 'A': 0, 'B': 2, 'C': 9 }


def test_djikstra_where_graph_has_a_heavy_weighted_node():
    subject = Graph()
    subject.add('A', 1)
    subject.add('B', 2, neighbors='A')
    subject.add('C', 3, neighbors='B')
    subject.add('D', 1335, neighbors='B')

    actual = subject.djikstra('A')
    assert actual == { 'A': 0, 'B': 2, 'C': 5, 'D': 1337 }


def test_djikstra_where_graph_is_complex():
    subject = Graph()
    subject.add('A', 1)
    subject.add('B', 6, neighbors='A')
    subject.add('C', 5, neighbors='B')
    subject.add('D', 1, neighbors=['A', 'B'])
    subject.add('E', 2, neighbors=['B', 'C', 'D'])

    actual = subject.djikstra('A')
    assert actual == { 'A': 0, 'B': 6, 'C': 8, 'D': 1, 'E': 3 }


def test_djikstra_where_graph_has_more_than_1_degree_of_separation():
    subject = Graph()
    subject.add('A', 1)
    subject.add('B', 2, neighbors='A')
    subject.add('C', 5, neighbors='B')
    subject.add('D', 1335, neighbors=['B'])
    subject.add('E', 3, neighbors=['D'])

    actual = subject.djikstra('A')
    assert actual == { 'A': 0, 'B': 2, 'C': 7, 'D': 1337, 'E': 1340 }
