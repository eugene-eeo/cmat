cmat
====

Elegant, tiny library for coloring entries in matrices::

    >>> from cmat.api import save, do, color_range, \
    ...     render, cols, rows
    >>> from random import random
    >>> M = [[random() for _ in range(10)] for _ in range(10)]
    >>> save(do(M,
    ...     color_range(M, cols[1:1] & rows[1:...]),
    ...     render
    ... ), 'data.html')

Internally most things are iterator based, so it is very easy to write
your own transforms and plug them into the pipeline.
