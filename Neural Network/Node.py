e = 2.71828


class Node:
    pass

    def __init__(self):
        self.X = [[0, 1, 2], [3, 4, 5]]

    def f(self, x):
        return [[1/(1+e**-x) for x in self.X] for y in range(len(self.X))]

    def fprime(self, x):
        return [(e**-x)/((1+e**-x)**2) for x in self.X]
