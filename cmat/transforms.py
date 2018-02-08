from collections import namedtuple
from .colorschemes import Color, interpolate
from .ranges import Pos, Rows


Entry = namedtuple('Entry', 'pos,value,color')


def begin(matrix):
    for i, row in enumerate(matrix):
        yield (Entry(Pos(i, j), x, Color('#FFF', '#000'))
               for j, x in enumerate(row))


def color_range(matrix, mask=Rows(0, ...), cs=None):
    lo = float('+inf')
    hi = float('-inf')
    for i, j in mask.gen(matrix):
        lo = min(matrix[i][j], lo)
        hi = max(matrix[i][j], hi)
    colorize = interpolate(cs, lo, hi)

    def iterator(entries):
        for row in entries:
            yield (Entry(entry.pos, entry.value, colorize(entry.value))
                   if entry.pos in mask
                   else entry
                   for entry in row)
    return iterator


def do(matrix, *ops):
    rv = begin(matrix)
    for f in ops:
        rv = f(rv)
    return rv


def format(v):
    if isinstance(v, int):
        return str(int(v))
    return '%f' % (v,)


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
