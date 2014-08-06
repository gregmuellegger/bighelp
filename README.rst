::

    >>> import H
    # Print stuff.
    >>> "hi" | H
    hi

    >>> # >> is always equivalent to |
    >>> "hi" >> H
    hi

    >>> # You can prefix things with H.
    >>> H << "hi"
    hi

    >>> # And all the three approaches are equivalent to:
    >>> H("hi")
    hi

    >>> import os.path
    >>> os.path.join | H
    Help on function join in module posixpath:

    join(a, *p)
        Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator.

    >>> os.path.join | H.code
    ... printing the source code for the method ...

    >>> os.path | H.code
    ... show source for module in pager since it's long output ...

    >>> # Slice the input.
    >>> [1, 2, 3] | H[1:]
    [2, 3]

    >>> # Filter dict if key starts with "a"
    >>> {'ab': 1, 'ac': 2, 'bc': 3} | H["a":]
    {'ab': 1, 'ac': 2}

    >>> # Filter dict if key ends with "c"
    >>> {'ab': 1, 'ac': 2, 'bc': 3} | H[:"c"]
    {'ac': 2, 'bc': 3}

    >>> dict() | H.dir
    ['__cmp__', ..., 'items', 'keys', ...]

You can trigger the debugger.
This sets a breakpoint for ``os.path.join``, whenever the function is
called, the debugger will fire up.

::

    >>> os.path.join | H.bp

    # Alias
    >>> os.path.join | H.breakpoint

    # Break now and invoke os.path.join
    >>> H.d(os.path.join, "a", "b")

    # Aliases.
    >>> H.debug(os.path.join, "a", "b")
    >>> H.pdb(os.path.join, "a", "b")

    # If the function does not take arguments, this also works with the pipe:
    >>> def two():
    ...     a = 1
    ...     b = 1
    ...     c = a + b
    ...     return c
    ...
    >>> two | H.d

Oh and exception handling, woot!

::

    >>> H.traceback
    # Prints traceback for current location. Useful when in debugger.

    >>> try:
    ...     1 / 0
    ... except Exception as exc:
    ...     exc | H
    ...
    # Shows traceback and all available information of the exception.
