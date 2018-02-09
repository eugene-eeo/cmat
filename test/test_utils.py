import pytest
from cmat.utils import ColsView


@pytest.fixture(params=[2,3,4,5])
def matrix(request):
     n = request.param
     M = []
     # Generates:
     #  | 1 1 1 1 |
     #  | 0 1 1 1 |
     #  | 0 0 1 1 |
     #  | 0 0 0 1 |
     for i in range(n):
          r = [0] * n
          r[i:] = [1] * (n-i)
          M.append(r)
     return M


def test_colsview_iter_getitem(matrix):
     n = len(matrix)
     for j in range(len(matrix)):
          c = ColsView(matrix, j)
          k = [1] * (j+1) + [0] * (n-1-j)
          assert list(c) == k
          for i, x in enumerate(k):
               assert c[i] == x


def test_colsview_len(matrix):
     n = len(matrix)
     for j in range(len(matrix)):
          c = ColsView(matrix[:j], 0)
          assert len(c) == j
