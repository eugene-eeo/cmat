import csv
import random
from cmat.api import rows, save, do, color_range, render, cols
from cmat.colorschemes import viridis, red_blue, pink

random.seed(0xDEADBEEF)
M = [[random.random() * 5 for _ in range(10)] for _ in range(10)]

save(do(
    M,
    color_range(M, rows[1:2], pink),
    render,
    ), '_example/1.html')

save(do(
    M,
    color_range(M, rows[1:2] | cols[1:2], pink),
    render,
    ), '_example/2.html')

save(do(
    M,
    color_range(M, rows[1:2] | cols[1:2], pink),
    color_range(M, cols[4:4], red_blue),
    color_range(M, rows[4:4], viridis),
    render,
    ), '_example/3.html')

save(do(
    M,
    color_range(M, rows[1:...] & cols[1:2], pink),
    color_range(M, rows[1:8] & cols[4:5], pink),
    color_range(M, rows[2:7] & cols[7:8], pink),
    render,
    ), '_example/4.html')


with open('_example/1545945', mode='r') as fp:
    table = []
    for i, row in enumerate(csv.reader(fp)):
        if i > 0:
            row[2:] = [float(x) for x in row[2:]]
        table.append(row)
    save(do(
        table,
        color_range(table, rows[1:...] & cols[16:16]),
        color_range(table, rows[1:...] & cols[24:24]),
        render,
        ), '_example/disease.html')
