from decimal import Decimal
from fractions import Fraction
from .colorschemes import Color, interpolate, red_blue
from .ranges import Pos, rows, Entry


def is_numeric(v):
    return isinstance(v, (int, float, Decimal, Fraction))


def begin(matrix):
    for i, row in enumerate(matrix):
        yield (Entry(matrix, Pos(i, j), Color('#FFF', '#000'))
               for j in range(len(row)))


def color_range(mask=rows[0:...], cs=red_blue):
    def iterator(matrix, entries):
        once = False
        lo = float('+inf')
        hi = float('-inf')
        for i, j in mask.gen(matrix):
            once = True
            x = matrix[i][j]
            if is_numeric(x):
                lo = min(x, lo)
                hi = max(x, hi)

        if not once:
            yield from entries
            return

        colorize = interpolate(cs, lo, hi)

        for row in entries:
            yield (entry.with_color(colorize(entry.value))
                   if (entry.pos in mask and is_numeric(entry.value))
                   else entry
                   for entry in row)
    return iterator


def do(matrix, *ops):
    rv = begin(matrix)
    for f in ops:
        rv = f(matrix, rv)
    return rv


def format(v):
    if isinstance(v, int):
        return str(int(v))
    if isinstance(v, (float, Decimal, Fraction)):
        return str(v)
    return str(v)


def render(_, rows):
    yield '<table cellpadding="2" border="1">'
    for row in rows:
        yield '<tr>'
        for entry in row:
            s = format(entry.value)
            td_fmt = '<td style="background-color:%s; color:%s">%s</td>'
            yield td_fmt % (entry.color.bg, entry.color.fg, s)
        yield '</tr>'
    yield '</table>'


def save(fname, render):
    with open(fname, 'w') as fp:
        for line in render:
            fp.write(line)
            fp.write('\n')
        fp.flush()
