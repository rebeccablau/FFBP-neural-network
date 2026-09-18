"""Creating abstract base class MultiLinkNode and its subclass Neurode."""
from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
import random


class MultiLinkNode(ABC):
    """Abstract base class for FFBPNeurode class."""

    class Side(Enum):
        """Enum class to identify relationships between nodes."""

        UPSTREAM = 1
        DOWNSTREAM = 2

    def __init__(self):
        """MultiLinkNode class constructor."""
        self._reporting_nodes = {MultiLinkNode.Side.UPSTREAM: 0,
                                 MultiLinkNode.Side.DOWNSTREAM: 0}
        self._reference_value = {MultiLinkNode.Side.UPSTREAM: 0,
                                 MultiLinkNode.Side.DOWNSTREAM: 0}
        self._neighbors = {MultiLinkNode.Side.UPSTREAM: [],
                           MultiLinkNode.Side.DOWNSTREAM: []}

    def __str__(self):
        """Return a string representation of the node in context."""
        node_string = f"Node: {id(self)}\n"

        node_string += "Node Upstream Neighbors:\n"
        for node in self._neighbors[MultiLinkNode.Side.UPSTREAM]:
            node_string += f"{id(node)}\n"

        node_string += "Node Downstream Neighbors:\n"
        for node in self._neighbors[MultiLinkNode.Side.DOWNSTREAM]:
            node_string += f"{id(node)}\n"

        return node_string

    @abstractmethod
    def _process_new_neighbor(self, node: MultiLinkNode, side: Side):
        """Assign a node a randomly assigned weight.

        Implemented in Neurode Class.
        """
        pass

    def reset_neighbors(self, nodes: list, side: Side):
        """Populate self._neighbors."""
        self._neighbors[side].clear()
        for node in nodes:
            self._neighbors[side].append(node)
            self._process_new_neighbor(node, side)

        self._reference_value[side] = ((2 ** len(nodes)) - 1)


class Neurode(MultiLinkNode):
    """Neurode class. Inherits from MultiLinkNode class."""

    _learning_rate = 0.05

    @property
    def learning_rate(self):
        """Get learning rate."""
        return Neurode._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """Set learning rate."""
        Neurode._learning_rate = learning_rate

    def __init__(self):
        """Neurode class constructor."""
        self._value = 0
        self._weights = {}
        super().__init__()

    def _process_new_neighbor(self, node: Neurode,
                              side: MultiLinkNode.Side):
        """Assign an upstream node a randomly assigned weight."""
        if side == MultiLinkNode.Side.UPSTREAM:
            self._weights[node] = (random.uniform(0, 1))

    def _check_in(self, node: Neurode, side: MultiLinkNode.Side):
        """Check if neighboring nodes are ready."""
        node_index = (self._neighbors[side].index(node))
        self._reporting_nodes[side] |= (2 ** node_index)
        if self._reporting_nodes[side] == self._reference_value[side]:
            self._reporting_nodes[side] = 0
            return True
        return False

    def get_weight(self, node: Neurode):
        """Return the weight of a given node."""
        return self._weights[node]

    @property
    def value(self):
        """Return the value of a node."""
        return self._value
