cmat
====

Elegant library for coloring entries in matrices::

    >>> from cmat.api import *
    >>> from random import random
    >>> M = [[random() for _ in range(10)] for _ in range(10)]
    >>> save(do(M,
    ...     color_range(cols[1:1] & rows[1:...]),
    ...     render
    ... ), 'data.html')

Internally most things are iterator based, so it is very easy to write
your own transforms and plug them into the pipeline. The aim is to
expose a nice API for creating quick and dirty scripts to visualise
matrices.

todo
----

- predicate functions
   - change internal Range interface
- write tests
- documentation
- gray color scheme
