def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true."""
    if function is None:
        def custom_filter():
            for elt in iterable:
                if elt is True:
                    yield elt
    else:
        def custom_filter():
            for elt in iterable:
                if function(elt) is True:
                    yield elt
    return custom_filter()
