def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print("List : ", end='')
    if type(object) is tuple:
        print("Tuple : ", end='')
    if type(object) is set:
        print("Set : ", end='')
    if type(object) is dict:
        print("Dict : ", end='')
    if type(object) is str:
        print("Brian is in the kitchen : ", end='')
    if type(object) is int:
        print("Type not found")
    else:
        print(type(object))
    return 42
