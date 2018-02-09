cmat
====

Elegant library for coloring entries in matrices::

    >>> from cmat.api import *
    >>> from random import random
    >>> M = [[random() for _ in range(10)] for _ in range(10)]
    >>> save(do(M,
    ...     color_range(cols[1:1] & rows[1:...]),
    ...     color_range(rows.where(M, lambda r: r[0] >= 0.5)),
    ...     render,
    ... ), 'data.html')

Internally most things are iterator based, so it is very easy to write
your own transforms and plug them into the pipeline. The aim is to
expose a nice API for creating quick and dirty scripts to visualise
matrices (read: tabular data).

todo
----

* predicate functions (√)

  * ``where(lambda x: x.value == "something")``
  * change internal Range interface

* write tests
* documentation
* gray color scheme
