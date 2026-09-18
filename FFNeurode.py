"""Creating the Feed-Forward Neurode class."""
from __future__ import annotations
from Neurode import Neurode
import numpy as np


class FFNeurode(Neurode):
    """Feed-Forward Neurode Class. Inherits from Neurode."""

    @staticmethod
    def _sigmoid(value: float):
        """Return the result of the sigmoid function at value."""
        return 1 / (1 + np.exp(-value))

    def _calculate_value(self):
        """Calculate value of upstream nodes using sigmoid function."""
        weighted_sum = 0
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            weighted_sum += node.value * self.get_weight(node)
        self._value = self._sigmoid(weighted_sum)

    def _fire_downstream(self):
        """Call data_ready_upstream on each downstream neighbor."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)

    def data_ready_upstream(self, node: Neurode):
        """Collect data from upstream nodes to make available to next layer."""
        if self._check_in(node, Neurode.Side.UPSTREAM):
            self._calculate_value()
            self._fire_downstream()

    def set_input(self, input_value: float):
        """Let the client set the value of an input layer node."""
        self._value = input_value
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)
