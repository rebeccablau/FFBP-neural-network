"""Creating the Neural Network Data Class."""
from enum import Enum
from collections import deque
import numpy as np
import random


class Order(Enum):
    """Enum class to define order of data."""

    SHUFFLE = 1
    STATIC = 2


class Set(Enum):
    """Enum class to decide if training or testing data is requested."""

    TRAIN = 1
    TEST = 2


class NNData:
    """Neural Network Data class."""

    @staticmethod
    def percentage_limiter(percentage: float):
        """Return percentage if given percentage is between 0 and 1.

        Return 0 if percentage is negative, or 1 if greater than 1.
        """
        if percentage < 0:
            return 0
        elif percentage > 1:
            return 1
        else:
            return percentage

    def __init__(self, features=None, labels=None, train_factor=0.9):
        """NNData constructor."""
        if features is None:
            features = []
        if labels is None:
            labels = []

        self._features = None
        self._labels = None
        self._train_factor = NNData.percentage_limiter(train_factor)
        self._train_indices = []
        self._test_indices = []
        self._train_pool = deque([])
        self._test_pool = deque([])

        self.load_data(features, labels)

    def load_data(self, features=None, labels=None):
        """Load or reload data."""
        if features is None or labels is None:
            self._features = None
            self._labels = None
            return self.split_set(self._train_factor)
        if len(features) != len(labels):
            self._features = None
            self._labels = None
            self.split_set(self._train_factor)
            raise ValueError
        try:
            self._features = np.array(features, dtype=float)
            self._labels = np.array(labels, dtype=float)
        except ValueError:
            self._features = None
            self._labels = None
            self.split_set(self._train_factor)
            raise ValueError

        self.split_set(self._train_factor)

    def split_set(self, new_train_factor=None):
        """Shuffle examples and assign them to testing or training.

        Do so according to training factor.
        """
        if new_train_factor is not None:
            self._train_factor = self.percentage_limiter(new_train_factor)

        if self._features is None:
            self._train_indices = []
            self._test_indices = []
        else:
            base_list = [i for i in range(len(self._features))]
            self._train_indices = random.sample(base_list,
                                                k=int(new_train_factor *
                                                      len(self._features)))
            self._test_indices = [i for i in base_list if i not in
                                  self._train_indices]

    def prime_data(self, target_set=None, order=None):
        """Reshuffle data for testing or training set, or both."""
        if target_set == Set.TRAIN or target_set is None:
            if order == Order.SHUFFLE:
                random.shuffle(self._train_indices)
            self._train_pool.clear()
            for item in self._train_indices:
                self._train_pool.append(item)
        if target_set == Set.TEST or target_set is None:
            if order == Order.SHUFFLE:
                random.shuffle(self._test_indices)
            self._test_pool.clear()
            for item in self._test_indices:
                self._test_pool.append(item)

    def get_one_item(self, target_set=None):
        """Deliver feature and label data from specified set."""
        if target_set == Set.TRAIN or target_set is None:
            if len(self._train_pool) == 0:
                return None
            index = self._train_pool.popleft()
            feature = self._features[index]
            label = self._labels[index]
            return feature, label
        if target_set == Set.TEST:
            if len(self._test_pool) == 0:
                return None
            index = self._test_pool.popleft()
            feature = self._features[index]
            label = self._labels[index]
            return feature, label

    def number_of_samples(self, target_set=None):
        """Return number of samples in one or both sets."""
        if target_set == Set.TEST:
            return len(self._test_indices)
        elif target_set == Set.TRAIN:
            return len(self._train_indices)
        else:
            return len(self._features)

    def pool_is_empty(self, target_set=None):
        """Return true is training or testing set is exhausted."""
        if target_set == Set.TEST:
            if len(self._test_pool) == 0:
                return True
        else:
            if len(self._train_pool) == 0:
                return True
        return False
