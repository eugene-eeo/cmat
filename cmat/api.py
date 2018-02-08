from .transforms import save, render, color_range, begin, do
from .ranges import Rows, Cols


__all__ = ['save', 'render', 'color_range', 'begin', 'do', 'rows', 'cols']


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
