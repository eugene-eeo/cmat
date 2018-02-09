from cmat.ranges import Rows, Pos, Cols


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
