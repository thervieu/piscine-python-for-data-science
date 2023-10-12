import sys


def count_print(text: str) -> None:
    """count_print(text: str)

    Counts different types of characters and prints the results."""
    print(f'The text contains {len(text)} characters:')
    print("{} upper letters".format(sum(1 for c in text if c.isupper())))
    print("{} lower letters".format(sum(1 for c in text if c.islower())))
    punct = "!\"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~"
    print("{} punctuation letters".format(sum(1 for c in text if c in punct)))
    print("{} spaces".format(sum(1 for c in text if c.isspace())))
    print("{} digits".format(sum(1 for c in text if c.isnumeric())))


def main() -> None:
    try:
        if len(sys.argv) > 2:
            raise Exception("AssertionError : more than one argument")
        if len(sys.argv) == 2:
            return count_print(sys.argv[1])
        print("What is the text to count?")
        return count_print(input()+" ")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
