from collections import namedtuple


Pos = namedtuple('Pos', 'i,j')


class Range:
    def __or__(self, other):
        return Union(self, other)

    def __and__(self, other):
        return Intersection(self, other)

    def __contains__(self, pos):
        raise NotImplementedError

    def gen(self, M):
        raise NotImplementedError


class Rows(Range):
    def __init__(self, a, b):
        self.a = a if a is not Ellipsis else float('-inf')
        self.b = b if b is not Ellipsis else float('+inf')

    def __contains__(self, pos):
        return self.a <= pos.i <= self.b

    def gen(self, M):
        for i in range(max(0, self.a), min(self.b+1, len(M))):
            for j in range(len(M[0])):
                yield Pos(i, j)


class Cols(Rows):
    def __contains__(self, pos):
        return self.a <= pos.j <= self.b

    def gen(self, M):
        for i in range(len(M)):
            for j in range(max(0, self.a), min(self.b+1, len(M[i]))):
                yield Pos(i, j)


class Intersection(Range):
    def __init__(self, *ranges):
        self.ranges = ranges

    def __contains__(self, pos):
        return all(pos in r for r in self.ranges)

    def __and__(self, other):
        if isinstance(other, Intersection):
            return Intersection(*self.ranges, *other.ranges)
        return Intersection(*self.ranges, other)

    def gen(self, M):
        for i, r in enumerate(self.ranges):
            c = self.ranges[:i]
            for pos in r.gen(M):
                # don't repeat points that have already been yielded, and
                # only yield if it is within all other ranges
                if not any(pos in r for r in c) and pos in self:
                    yield pos


class Union(Range):
    def __init__(self, *ranges):
        self.ranges = ranges

    def __contains__(self, pos):
        return any(pos in r for r in self.ranges)

    def __or__(self, other):
        if isinstance(other, Union):
            return Union(*self.ranges, *other.ranges)
        return Union(*self.ranges, other)

    def gen(self, M):
        for i, r in enumerate(self.ranges):
            c = self.ranges[:i]
            for pos in r.gen(M):
                if not any(pos in r for r in c):
                    yield pos


class _R:
    def __getitem__(self, a):
        if isinstance(a, int):
            return Rows(a, a)
        return Rows(a.start, a.stop)


class _C:
    def __getitem__(self, a):
        if isinstance(a, int):
            return Cols(a, a)
        return Cols(a.start, a.stop)


rows = _R()
cols = _C()
