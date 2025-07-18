import csv
from .series import Series
from .index import Index

class DataFrame:
    """Represents the data table."""

    def __init__(self, values, columns = None):
        """Creats dataframe with given values and columns."""

        if not values:
            raise ValueError("Values must contain at least one element.")
        
        self.values = values

        if not columns:
            labels = range(len(values))
            columns = Index(labels)

        if len(columns.labels) != len(values):
            raise ValueError(f"Columns and values are not the same length.\nColumns length: {len(columns.labels)}\nValues length:{len(values)}")

        self.columns = columns
    
    def __len__(self):
        return len(self.columns)

    def __iter__(self):
        yield from self.columns

    def __getitem__(self, key):
        return self.values[self.columns.get_loc(key)]

    def __repr__(self):
        return f"DataFrame{self.shape}"
    
    def __str__(self):
        return self.__repr__()
    
    @classmethod
    def from_csv(cls, csv_file, separator):
        """Creates Dataframe class from csv file."""

        with csv_file.open(mode="r") as file:
            csv_reader = csv.reader(file, delimiter=separator)
            splitted = [row for row in csv_reader]
            labels = list(filter(None, splitted.pop(0)))
            columns = list(zip(*splitted))
            index = Index(list(columns.pop(0)))
    
        return cls([Series(list(column), index) for column in columns], Index(labels))

    @property
    def shape(self):
        """Returns shape of given dataframe."""
        return (len(self.values[0]), len(self.columns))

    def items(self):
        """Returns iterator."""
        return zip(self.columns, self.values)

    def index(self):
        return self.values[0].index

    def get(self, key):
        """Returns matching value to given key."""
        
        try:
            result = self[key]
        except KeyError as err:
            return None

        return result