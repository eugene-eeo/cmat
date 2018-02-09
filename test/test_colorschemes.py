import pytest
from cmat.colorschemes import interpolate, Color


def gen_cs(n):
     return [Color(i, i) for i in range(n)]


c2 = gen_cs(2)
c4 = gen_cs(4)


@pytest.mark.parametrize('cs,x,expected', [
     (c2, 0.00, c2[0]),
     (c2, 1.00, c2[1]),
     (c4, 0.00, c4[0]),
     (c4, 0.25, c4[0]),
     (c4, 0.50, c4[1]),
     (c4, 0.51, c4[1]),
     (c4, 0.75, c4[2]),
     (c4, 0.80, c4[2]),
     (c4, 1.00, c4[3]),
])
def test_interpolate(cs, x, expected):
     s = interpolate(cs, 0, 1)
     assert s(x) == expected
