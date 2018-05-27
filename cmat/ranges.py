from collections import namedtuple
from .utils import ColsView


Pos = namedtuple('Pos', 'i,j')


class Entry(namedtuple('Entry', 'data,pos,color')):
    @property
    def value(self):
        return self.data[self.pos.i][self.pos.j]

    def with_color(self, color):
        return Entry(self.data, self.pos, color)


class Range:
    def __or__(self, other):
        return Union(self, other)

    def __and__(self, other):
        return Intersection(self, other)

    def __contains__(self, entry):
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
        # only yield if it is within all other ranges
        for pos in self.ranges[0].gen(M):
            if pos in self:
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
                # if we haven't seen this position before then yield it
                if not any(pos in r for r in c):
                    yield pos


class OkSet(Range):
    def __init__(self, cols=None, rows=None):
        self.cols = cols
        self.rows = rows

    def __contains__(self, pos):
        return (
            (self.rows is None or pos.i in self.rows) and
            (self.cols is None or pos.j in self.cols)
            )

    def gen(self, M):
        for i in (self.rows or range(len(M))):
            if i >= len(M):
                continue
            for j in (self.cols or range(len(M[i]))):
                if j < len(M[i]):
                    yield Pos(i, j)


class _R:
    def __getitem__(self, a):
        if isinstance(a, int):
            return Rows(a, a)
        return Rows(a.start, a.stop)

    def where(self, M, f):
        ok = set()
        for i, row in enumerate(M):
            if f(row):
                ok.add(i)
        return OkSet(rows=ok)


class _C:
    def __getitem__(self, a):
        if isinstance(a, int):
            return Cols(a, a)
        return Cols(a.start, a.stop)

    def where(self, M, f):
        ok = set()
        for j in range(len(M[0])):
            if f(ColsView(M, j)):
                ok.add(j)
        return OkSet(cols=ok)


rows = _R()
cols = _C()
