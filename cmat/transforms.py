from collections import namedtuple
from decimal import Decimal
from fractions import Fraction
from .colorschemes import Color, interpolate, red_blue
from .ranges import Pos, rows


Entry = namedtuple('Entry', 'pos,value,color')


def is_numeric(v):
    return isinstance(v, (int, float, Decimal, Fraction))


def begin(matrix):
    for i, row in enumerate(matrix):
        yield (Entry(Pos(i, j), x, Color('#FFF', '#000'))
               for j, x in enumerate(row))


def color_range(matrix, mask=rows[0:...], cs=red_blue):
    lo = float('+inf')
    hi = float('-inf')
    for i, j in mask.gen(matrix):
        x = matrix[i][j]
        if is_numeric(x):
            lo = min(x, lo)
            hi = max(x, hi)
    colorize = interpolate(cs, lo, hi)

    def iterator(entries):
        for row in entries:
            yield (Entry(e.pos, e.value, colorize(e.value))
                   if (e.pos in mask and is_numeric(e.value))
                   else e
                   for e in row)
    return iterator


def do(matrix, *ops):
    rv = begin(matrix)
    for f in ops:
        rv = f(rv)
    return rv


def format(v):
    if isinstance(v, int):
        return str(int(v))
    if isinstance(v, (float, Decimal, Fraction)):
        return str(v)
    return str(v)


def render(rows):
    yield '<table cellpadding="2" border="1">'
    for row in rows:
        yield '<tr>'
        for entry in row:
            s = format(entry.value)
            td_fmt = '<td style="background-color:%s; color:%s">%s</td>'
            yield td_fmt % (entry.color.bg, entry.color.fg, s)
        yield '</tr>'
    yield '</table>'


def save(render, f):
    with open(f, 'w') as fp:
        for line in render:
            fp.write(line)
            fp.write('\n')
        fp.flush()
