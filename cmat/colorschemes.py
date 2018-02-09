from collections import namedtuple


Color = namedtuple('Color', 'bg,fg')


red_blue = [
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

viridis = [
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

pink = [
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


def interpolate(colorscheme, lo, hi):
    N = len(colorscheme) - 1
    B = hi - lo

    def scale(x):
        return colorscheme[int(N * (x - lo)/B)]
    return scale
