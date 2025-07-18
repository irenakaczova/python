import csv
import statistics
import operator
from .index import Index

class Series:
    """Contains a sequence of values indexed by an object of class Index."""

    def __init__(self, values, index = None):
        """Creates series with given values and index."""

        if not values:
            raise ValueError("Values must contain at least one element.")
        
        self.values = values

        if not index:
            labels = range(len(values))
            index = Index(labels)

        if len(index.labels) != len(values):
            raise ValueError(f"Index and values are not the same length.\nIndex length: {len(index.labels)}\nValues length:{len(values)}")

        self.index = index

    def __len__(self):
        return len(self.values)
    
    def __iter__(self):
        yield from self.values

    def __getitem__(self, key):
        return self.values[self.index.get_loc(key)]

    def __repr__(self):
        return "\n".join([f"{index}\t{repr(value)}" for index, value in zip(self.index.labels, self.values)])
    
    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return self._apply_operator(other, operator.add)

    def __sub__(self, other):
        return self._apply_operator(other, operator.sub)

    def __mul__(self, other):
        return self._apply_operator(other, operator.mul)

    def __truediv__(self, other):
        return self._apply_operator(other, operator.truediv)

    def __floordiv__(self, other):
        return self._apply_operator(other, operator.floordiv)

    def __mod__(self, other):
        return self._apply_operator(other, operator.mod)

    def __pow__(self, other):
        return self._apply_operator(other, operator.pow)

    def __round__(self, precision):
        """Applies round function with given precision to all the elements of the sequence and returns new series with obtained values."""
        return self.apply(round, precision)

    @classmethod
    def from_csv(cls, csv_file, separator):
        """Creates Series class from csv file."""

        with csv_file.open(mode="r") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            labels, values = [row for row in csv_reader]

        return cls(values, Index(labels))
    
    @property
    def shape(self):
        """Returns shape of given serie."""
        return (len(self.values),)
    
    def _apply_operator(self, other, operator):
        if not isinstance(other, Series):
            raise TypeError(f"Other must be of type Series.\nGiven type: {type(other)}")

        if len(self.values) != len(other.values):
            raise ValueError(f"Self and other are not the same length.\nSelf length: {len(self.values)}\nOther length:{len(other.values)}")
        
        return Series([operator(number_x, number_y) for number_x, number_y in zip(*[(self.values), (other.values)])], self.index)

    def get(self, key):
        """Returns matching value to given key."""
        
        try:
            result = self[key]
        except KeyError as err:
            return None

        return result

    def items(self):
        """Returns iterator."""
        return zip(self.index.labels, self.values)

    def sum(self):
        """Sums all the values of the sequence."""
        return sum(self.values)

    def max(self):
        """Finds the maximum value of the sequence."""
        return max(self.values)

    def min(self):
        """Finds the minimum value of the sequence."""
        return min(self.values)

    def mean(self):
        """Returns the mean value of the sequence."""
        return statistics.mean(self.values)

    def apply(self, func, *args):
        """Applies given function to all the elements of the sequence and returns new series with obtained values."""
        return Series([func(number, *args) for number in (self.values)], self.index)

    def abs(self):
        """Returns new series with the abs values of elements from the given sequence."""
        return self.apply(abs)