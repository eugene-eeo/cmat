class ColsView:
    def __init__(self, matrix, column):
        self.m = matrix
        self.j = column

    def __iter__(self):
        for i in range(len(self.m)):
            yield self.m[i][self.j]

    def __getitem__(self, i):
        if isinstance(i, slice):
            return [a[self.j] for a in self.m[i]]
        return self.m[i][self.j]

    def __len__(self):
        return len(self.m)
