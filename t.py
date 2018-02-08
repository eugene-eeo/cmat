import random
from cmat.api import rows, save, do, color_range, render, cols
from cmat.colorschemes import viridis, red_blue, pink

random.seed(0xDEADBEEF)

f = lambda: random.random() * 5
M = [[f() for _ in range(10)] for _ in range(10)]

save(do(M, color_range(M, cs=red_blue), render), '_example/1.html')
save(do(M, color_range(M, cs=viridis), render),  '_example/2.html')
save(do(M, color_range(M, cs=pink), render),     '_example/3.html')

save(do(
    M,
    color_range(M, rows[1:2], pink),
    render,
    ), '_example/4.html')

save(do(
    M,
    color_range(M, rows[1:2] | cols[1:2], pink),
    render,
    ), '_example/5.html')

save(do(
    M,
    color_range(M, rows[1:2] | cols[1:2], pink),
    color_range(M, cols[4:4], red_blue),
    color_range(M, rows[4:4], viridis),
    render,
    ), '_example/5.html')

save(do(
    M,
    color_range(M, rows[1:...] & cols[1:2], pink),
    color_range(M, rows[1:8] & cols[4:5], pink),
    color_range(M, rows[2:7] & cols[7:8], pink),
    render,
    ), '_example/6.html')

save(do(
    M[:4],
    color_range(M, rows[1:...] & cols[1:2], pink),
    render,
    ), '_example/7.html')
