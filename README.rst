cmat
====

Elegant library for coloring entries in matrices::

    >>> from cmat.api import *
    >>> from random import random
    >>> M = [[random() for _ in range(10)] for _ in range(10)]
    >>> save('data.html', do(M,
    ...     color_range(cols[1:1] & rows[1:...]),
    ...     color_range(rows.where(M, lambda r: r[0] >= 0.5)),
    ...     render,
    ... ))

Internally most things are iterator based, so it is very easy to write
your own transforms and plug them into the pipeline. The aim is to
expose a nice API to let one write quick and dirty scripts to visualise
matrices (read: tabular data).

todo
----

* implement proper color interpolation
* write tests
* documentation
* gray color scheme
