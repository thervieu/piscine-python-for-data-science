def slice_me(family: list, start: int, end: int) -> list:
    first_len = 0
    if family[0] is not None:
        first_len = len(family[0])
    for arr in family[1:len(family)]:
        if len(arr) != first_len:
            raise ValueError("family has different length rows")
    if abs(start) > len(family):
        raise ValueError("start higher than len of array")
    if abs(end) > len(family):
        raise ValueError("end higher than len of array")

    print(f'My shape is {len(family), len(family[0])}')
    
    newfamily = family[start:end]
    print(f'My new shape is {len(family), len(family[0])}')

    return newfamily
    