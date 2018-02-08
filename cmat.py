from collections import namedtuple


Pos   = namedtuple('Pos',   'i,j')
Color = namedtuple('Color', 'bg,fg')
Entry = namedtuple('Entry', 'pos,value,color')


COLORS = [
    Color('#053061', '#FFFFFF'),
    Color('#2166ac', '#FFFFFF'),
    Color('#4393c3', '#FFFFFF'),
    Color('#92c5de', '#000000'),
    Color('#d1e5f0', '#000000'),
    Color('#f7f7f7', '#000000'),
    Color('#fddbc7', '#000000'),
    Color('#f4a582', '#000000'),
    Color('#d6604d', '#FFFFFF'),
    Color('#b2182b', '#FFFFFF'),
    Color('#67001f', '#FFFFFF'),
]

COLORS2 = [
    Color('#f7fcf0', '#000000'),
    Color('#e0f3db', '#000000'),
    Color('#ccebc5', '#000000'),
    Color('#a8ddb5', '#000000'),
    Color('#7bccc4', '#000000'),
    Color('#4eb3d3', '#000000'),
    Color('#2b8cbe', '#FFFFFF'),
    Color('#0868ac', '#FFFFFF'),
    Color('#084081', '#FFFFFF'),
]

COLORS3 = [
    Color('#fff7f3', '#000000'),
    Color('#fde0dd', '#000000'),
    Color('#fcc5c0', '#000000'),
    Color('#fa9fb5', '#000000'),
    Color('#f768a1', '#000000'),
    Color('#dd3497', '#FFFFFF'),
    Color('#ae017e', '#FFFFFF'),
    Color('#7a0177', '#FFFFFF'),
    Color('#49006a', '#FFFFFF'),
]


def cmap(colorscheme, hi, lo):
    N = len(colorscheme) - 1

    def scale(d):
        return colorscheme[int(N * (d - lo) / (hi - lo))]
    return scale


def elp(k, default):
    if k is Ellipsis:
        return default
    return k


def cols(a, b):
    a = elp(a, float('-inf'))
    b = elp(b, float('+inf'))

    def is_within(i, j):
        return a <= j <= b

    def gen(M):
        for j in range(max(0, a), min(b+1, len(M[0]))):
            for i in range(len(M)):
                yield i, j

    return is_within, gen


def rows(a, b):
    a = elp(a, float('-inf'))
    b = elp(b, float('+inf'))

    def is_within(i, j):
        return a <= i <= b

    def gen(M):
        for i in range(max(0, a), min(b+1, len(M))):
            for j in range(len(M[0])):
                yield i, j

    return is_within, gen


def intersection(*pairs):
    def is_within(i, j):
        return all(is_within(i, j) for is_within, _ in pairs)

    def gen(M):
        for i, (_, gen) in enumerate(pairs):
            c = pairs[:i]
            for i, j in gen(M):
                if not any(yielded(i, j) for yielded, _ in c) and \
                       is_within(i, j):
                    yield (i, j)

    return is_within, gen


def union(*pairs):
    def is_within(i, j):
        return any(is_within(i, j) for is_within, _ in pairs)

    def gen(M):
        for i, (_, gen) in enumerate(pairs):
            c = pairs[:i]
            for i, j in gen(M):
                if not any(is_within(i, j) for is_within, _ in c):
                    yield (i, j)

    return is_within, gen


def begin(data):
    for i, row in enumerate(data):
        yield (Entry(Pos(i, j), x, Color('#FFFFFF','#000000'))
               for j, x in enumerate(row))


def color_range(data, mask=None, cs=COLORS):
    if mask is None:
        mask = union(rows(0, len(data)-1), cols(0, len(data[0])-1))

    is_within, gen = mask
    hi = float('-inf')
    lo = float('+inf')
    for i, j in gen(data):
        hi = max(data[i][j], hi)
        lo = min(data[i][j], lo)
    scale = cmap(cs, hi, lo)

    def iterator(entries):
        for row in entries:
            yield (Entry(entry.pos, entry.value, scale(entry.value))
                   if is_within(*entry.pos)
                   else entry
                   for entry in row)
    return iterator


def do(matrix, *ops):
    it = begin(matrix)
    for f in ops:
        it = f(it)
    return it


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
