from ft_filter import ft_filter


def isEven(nb) -> bool:
    if nb % 2 == 0:
        return True
    return False


def main():
    print(ft_filter.__doc__)

    mylist = [1, 2, 3, 4, 5]
    print()
    print("filtering even numbers")
    print(mylist)
    print([elt for elt in ft_filter(isEven, mylist)])
    print([elt for elt in filter(isEven, mylist)])

    print()
    print("filtering w/o funtion")

    mylistBool = [True, False, True, False, False]
    print(mylistBool)
    print([elt for elt in ft_filter(None, mylistBool)])
    print([elt for elt in filter(None, mylistBool)])


if __name__ == "__main__":
    main()
