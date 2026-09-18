"""Root Mean Sqaure Error classes."""
from abc import ABC, abstractmethod
import math
import copy


class RMSE(ABC):
    """Room Mean Square Error abstract base class."""

    def __init__(self):
        """RMSE class constructor."""
        self._predicted_values = []
        self._expected_values = []

    def __add__(self, other):
        """Add predicted and expected values."""
        predicted_value, expected_value = other
        new_object = copy.deepcopy(self)
        new_object._predicted_values.append(predicted_value)
        new_object._expected_values.append(expected_value)
        return new_object

    def __iadd__(self, other):
        """Add predicted and expected values."""
        predicted_value, expected_value = other
        self._predicted_values.append(predicted_value)
        self._expected_values.append(expected_value)
        return self

    def reset(self):
        """Clear all internal data."""
        self._predicted_values.clear()
        self._expected_values.clear()

    @property
    def error(self):
        """Calculate and return the RMSE."""
        if len(self._expected_values) == 0:
            return 0

        rmse_value = 0
        for item in zip(self._predicted_values, self._expected_values):
            rmse_value += self.distance(item[0], item[1]) ** 2
        rmse_value /= len(self._expected_values)
        return math.sqrt(rmse_value)

    @staticmethod
    @abstractmethod
    def distance(point_one, point_two):
        """Calculate the distance between two points (tuples)."""
        pass


class Euclidean(RMSE):
    """Euclidean distance class, inherits from RMSE class."""

    @staticmethod
    def distance(point_one, point_two):
        """Return the Euclidean distance between two points (tuples)."""
        euclidean_distance = 0
        for p1, p2 in zip(point_one, point_two):
            euclidean_distance += ((p1 - p2) ** 2)
        return math.sqrt(euclidean_distance)


class Taxicab(RMSE):
    """Taxicab distance class, inherits from RMSE class."""

    @staticmethod
    def distance(point_one, point_two):
        """Return the Taxicab distance between two points (tuples)."""
        taxicab_distance = 0
        for p1, p2 in zip(point_one, point_two):
            taxicab_distance += math.fabs(p1 - p2)
        return taxicab_distance
