"""Creating the Backpropagation Neurode class."""
from Neurode import Neurode


class BPNeurode(Neurode):
    """Backpropagation Neurode class. Inherits from Neurode."""

    def __init__(self):
        """BPNeurode constructor."""
        self._delta = 0
        super().__init__()

    @staticmethod
    def _sigmoid_derivative(value: float):
        """Calculate the derivative of the sigmoid function."""
        return value * (1 - value)

    def _calculate_delta(self, expected_value: float = None):
        """Calculate the delta of the Neurode."""
        if len(self._neighbors[Neurode.Side.DOWNSTREAM]) == 0:
            self._delta = ((expected_value - self.value) *
                           self._sigmoid_derivative(self.value))
        else:
            weighted_sum = 0
            for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
                weighted_sum += node.get_weight(self) * node.delta
            self._delta = weighted_sum * self._sigmoid_derivative(self.value)

    def data_ready_downstream(self, node: Neurode):
        """Collect data from downstream nodes and pass to next layer up."""
        if self._check_in(node, Neurode.Side.DOWNSTREAM):
            self._calculate_delta()
            self._fire_upstream()
            self._update_weights()

    def set_expected(self, expected_value: float):
        """Set expected value of an output layer neurode."""
        self._calculate_delta(expected_value)
        self._fire_upstream()

    def adjust_weights(self, node: Neurode, adjustment: float):
        """Adjust the weight of a given neurode."""
        self._weights[node] += adjustment

    def _update_weights(self):
        """Update the weights of downstream neighbors."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            adjustment = self.value * node.delta * node.learning_rate
            node.adjust_weights(self, adjustment)

    def _fire_upstream(self):
        """Call data_ready_downstream on each upstream neighbor."""
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    @property
    def delta(self):
        """Return the delta of a node."""
        return self._delta
