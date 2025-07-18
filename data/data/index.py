class Index:
    """Indexes the sequence of values."""

    def __init__(self, labels, name = ""):
        """Creates index with given labels and name."""

        if not labels:
            raise ValueError("Labels must contain at least one element.")
        
        if len(labels) != len(set(labels)):
            raise ValueError(f"There are duplicates in labels: {labels}.")

        self.labels = labels
        self.name = name

    def __len__(self):
        return len(self.labels)

    def __iter__(self):
        yield from self.labels

    def get_loc(self, key):
        """Translates given key to matching index."""

        try:
            idx = self.labels.index(key)
        except ValueError as err:
            raise KeyError(f"{key} not found in {self.labels}.")
        
        return idx