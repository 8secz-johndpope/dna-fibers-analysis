"""
Model management of the DNA fiber analysis package.

Use this module to use the default model, create custom models and use the
convenience tools for models management.
"""
import numpy as np


class Model:
    """
    Pattern model management.

    This is a convenience class used for model management. Once the model of
    patterns is set (see below), it can be saved and patterns can be simulated
    randomly from it. It can also be loaded from file.

    A model is a list of pattern structures. Pattern structure is a dictionary
    with the following keys:
    - 'name': the name of the pattern (ex: 'ongoing fork')
    - 'freq': its frequency of appearance (ex: 0.7)
    - 'channels': its actual pattern of channels (ex: [0, 1])
    - 'mean': the mean length of branches (ex: [100, 90])
    - 'std': the standard deviation of branches (ex: [10, 5])
    """
    def __init__(self, patterns):
        """
        Initialize the model with the specified patterns.

        :param patterns: List of patterns.
        :type patterns: list of dict
        """
        self.patterns = patterns

        self._update_frequencies()
        self._normalize_frequencies()

    def _update_frequencies(self):
        """
        Update the class shortcut for patterns frequencies.
        """
        self._frequencies = [pattern['freq'] for pattern in self.patterns]

    def _normalize_frequencies(self):
        """
        Normalize the patterns frequencies.
        """
        for pattern in self.patterns:
            pattern['freq'] /= self._frequencies

        self._update_frequencies()

    def save(self, filename):
        raise RuntimeError('Not yet implemented!')

    @staticmethod
    def load(filename):
        raise RuntimeError('Not yet implemented!')

    def simulate_patterns(self, number):
        """
        Simulate number patterns.

        :param number: Number of patterns to simulate.
        :type number: int

        :return: The channels (the patterns branch) and the lengths (the
        branches lengths).
        :rtype:list of list of int and list of list of float
        """
        patterns = np.random.choice(self.patterns, number, p=self._frequencies)

        channels, lengths = [], []

        for pattern in patterns:
            channels.append(pattern['channels'])

            lengths.append([std * np.random.randn() + mean
                            for mean, std in
                            zip(pattern['mean'], pattern['std'])])

        return channels, lengths


standard = Model([
    {'name': 'ongoing fork',
     'freq': 0.7,
     'channels': [0, 1],
     'mean': [100, 90],
     'std': [10, 5]},
])
