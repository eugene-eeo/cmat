import csv
from cmat.api import rows, save, do, color_range, render, cols
from cmat.colorschemes import red_blue, pink

with open('_example/1545945', mode='r') as fp:
    table = []
    for i, row in enumerate(csv.reader(fp)):
        if i > 0:
            row[2:] = [float(x) for x in row[2:]]
        table.append(row)
    save(do(
        table,
        color_range(rows[1:...] & cols[16:16], red_blue),
        color_range(rows[1:...] & cols[24:24], red_blue),
        # compare between three different countries
        color_range(rows[20:20] | rows[21:21] | rows[30:30], pink),
        render,
        ), '_example/disease.html')
