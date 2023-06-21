import sys


def filterstring():
    if len(sys.argv) != 3:
        return print("AssertionError : the arguments are bad")
    word_size = 0
    try:
        word_size = int(sys.argv[2])
        non_print_or_punct = lambda c : c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" != 0 or c.isprintable
        if sum(1 for c in sys.argv[1] if non_print_or_punct(c)):
            raise Exception("")
    except Exception:
        return print("AssertionError : the arguments are bad")
    return print(elt for elt in sys.argv[1].split() if len(elt) > word_size) 


if __name__ == "__main__":
    filterstring()
