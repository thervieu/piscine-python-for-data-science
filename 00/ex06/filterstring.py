import sys


def filterstring():
    """filterstring() -> None

    Prints the words of the first argument
    if their length is superior or equal to the first argument """

    word_size = 0
    try:
        if len(sys.argv) != 3:
            raise Exception("AssertionError : wrong number of arguments")
        word_size = int(sys.argv[2])
        p = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        bacChar = lambda c: c in p != 0 or c.isprintable is False
        if sum(1 for c in sys.argv[1] if bacChar(c)):
            raise Exception("AssertionError : string is wrong")
        is_min_size = lambda c: len(c) > word_size
        return print([elt for elt in sys.argv[1].split() if is_min_size(elt)])
    except Exception as e:
        return print(e)


if __name__ == "__main__":
    filterstring()
