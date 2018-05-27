import pytest
from itertools import product
from cmat.ranges import Rows, Pos, Cols, OkSet


def test_rows():
     r = Rows(1, 3)
     for j in range(10):
          assert Pos(0, j) not in r
          assert Pos(1, j) in r
          assert Pos(2, j) in r
          assert Pos(3, j) in r
          assert Pos(4, j) not in r


def test_cols():
     r = Cols(1, 3)
     for i in range(10):
          assert Pos(i, 0) not in r
          assert Pos(i, 1) in r
          assert Pos(i, 2) in r
          assert Pos(i, 3) in r
          assert Pos(i, 4) not in r


def test_intersection():
     r = Rows(1, 3) & Cols(1, 2)
     for i in range(5):
          for j in range(5):
               if 1 <= i <= 3 and 1 <= j <= 2:
                    assert Pos(i, j) in r


def test_union():
     r = Rows(1, 3) | Cols(1, 2)
     for i in range(5):
          for j in range(5):
               if 1 <= i <= 3 or 1 <= j <= 2:
                    assert Pos(i, j) in r


def test_nested():
     r = (Rows(1, 1) | Rows(3, 3)) & Cols(1, 1)
     assert Pos(1, 1) in r
     assert Pos(3, 1) in r
     assert Pos(1, 2) not in r
     assert Pos(3, 2) not in r
     assert Pos(2, 1) not in r


@pytest.fixture(params=[
     (None,    None),
     ({1},     {}),
     ({},      {1}),
     ({1,2},   {0,1,2,3}),
     ({5,1,2}, {10}),
])
def row_col_set(request):
     return request.param


def test_okset_contains(row_col_set):
     rows, cols = row_col_set
     r = OkSet(rows=rows, cols=cols)

     rows = {0, 1, 2} if rows is None else {}
     cols = {0, 1, 2} if cols is None else {}

     for i, j in product(rows, cols):
          assert Pos(i, j) in r


def test_okset_gen(row_col_set):
     rows, cols = row_col_set
     rows = rows or {0, 1, 2}
     cols = cols or {0, 1, 2}

     r = OkSet(rows=rows, cols=cols)
     M = [[1,1,1]] * 3

     for i, j in product(rows, cols):
          if 0 < i < 3 and 0 < j < 3:
               assert Pos(i, j) in r.gen(M)
