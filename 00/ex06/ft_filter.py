def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true."""
    return [elt for elt in iterable if function(elt) == True]
