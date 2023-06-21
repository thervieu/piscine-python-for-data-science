def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing :", object, end='')
    if type(object) is float:
        print("Cheese :", object, end='')
    if type(object) is int:
        print("Zero :", object, end='')
    if type(object) is bool:
        print("Fake :", object, end='')
    if type(object) is str and object=='':
        print("Empty :", end='')
    if type(object) is str and object!='':
        print("Type not Found")
    else:
        print("", type(object))
    return 1
