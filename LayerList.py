"""LayerList class, an extension of DoublyLinkedList."""
from DoublyLinkedList import DoublyLinkedList
from Neurode import Neurode


class LayerList(DoublyLinkedList):
    """LayerList class."""

    @staticmethod
    def link_nodes(layer_1, layer_2):
        """Link the neurodes in the neighboring layers."""
        for neurode in layer_1:
            neurode.reset_neighbors(layer_2, neurode.Side.DOWNSTREAM)
        for neurode in layer_2:
            neurode.reset_neighbors(layer_1, neurode.Side.UPSTREAM)

    def __init__(self, inputs: int, outputs: int, neurode_type: type(Neurode)):
        """LayerList constructor."""
        super().__init__()

        self._input_neurodes = [neurode_type() for _ in range(inputs)]
        self._output_neurodes = [neurode_type() for _ in range(outputs)]
        self._neurode_type = neurode_type

        self.link_nodes(self._input_neurodes, self._output_neurodes)

        self.add_to_head(self._input_neurodes)
        self.add_after_current(self._output_neurodes)

    def add_layer(self, num_nodes: int):
        """Add a layer of neurodes to the linked list."""
        if self._curr == self._tail:
            raise IndexError

        new_layer = [self._neurode_type() for _ in range(num_nodes)]
        self.add_after_current(new_layer)

        self.link_nodes(self._curr.data, self._curr.next.data)
        self.link_nodes(self._curr.next.data, self._curr.next.next.data)

    def remove_layer(self):
        """Remove a layer of neurodes from the linked list."""
        if self._curr.next == self._tail:
            raise IndexError

        self.remove_after_current()
        self.link_nodes(self._curr.data, self._curr.next.data)

    @property
    def input_nodes(self):
        """Return the input nodes."""
        return self._input_neurodes

    @property
    def output_nodes(self):
        """Return the output nodes."""
        return self._output_neurodes
