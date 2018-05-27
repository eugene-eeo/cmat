import csv
from cmat.api import save, rows, cols, do, color_range, render
from cmat.colorschemes import red_blue, pink, viridis


with open('_example/1545945', mode='r') as fp:
    table = []
    for i, row in enumerate(csv.reader(fp)):
        if i > 0:
            row[2:] = [float(x) for x in row[2:]]
        table.append(row)
    save('_example/disease.html', do(
        table,
        color_range(rows[1:...] & cols[16]),
        # pick a color scheme
        color_range(rows[1:...] & cols[24], red_blue),
        # compare between three different countries
        color_range(rows.where(table, lambda r: (r[0] in ['CMR', 'BRA', 'BRN'])),
                    pink),
        # compare between two diseases
        color_range(cols.where(table, lambda c: (c[0] in ["disa2","disa3"])), viridis),
        color_range(
            rows.where(table, lambda r: ('TUN' <= r[0] <= 'TZA')) &
            cols.where(table, lambda c: ('disa2' <= c[0] <= 'disa5')),
            pink,
            ),
        render,
        ))
