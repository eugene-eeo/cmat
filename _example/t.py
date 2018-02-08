import random
from cmat import *

random.seed(0xDEADBEEF)

f = lambda: random.random() * 5
M = [[f() for _ in range(10)] for _ in range(10)]

save(do(M, color_range(M, cs=COLORS), render), '1.html')
save(do(M, color_range(M, cs=COLORS2), render), '2.html')
save(do(M, color_range(M, cs=COLORS3), render), '3.html')

save(do(
    M,
    color_range(M, rows(1,2), COLORS3),
    render,
    ), '4.html')

save(do(
    M,
    color_range(M, union(rows(1,2), cols(1,2)), COLORS3),
    render,
    ), '5.html')

save(do(
    M,
    color_range(M, union(rows(1,2), cols(1,2)), COLORS3),
    color_range(M, union(cols(4,4)), COLORS),
    color_range(M, union(rows(4,4)), COLORS2),
    render,
    ), '5.html')

save(do(
    M,
    color_range(M, intersection(rows(1,...), cols(1,2)), COLORS3),
    color_range(M, intersection(rows(1,8), cols(4,5)), COLORS3),
    color_range(M, intersection(rows(2,7), cols(7,8)), COLORS3),
    render,
    ), '6.html')
