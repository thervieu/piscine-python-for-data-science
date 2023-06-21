import sys

def count_print(text: str) -> None:
    print(f'The text contains {len(text)} characters:')
    print("{} upper letters".format(sum(1 for c in text if c.isupper())))
    print("{} lower letters".format(sum(1 for c in text if c.islower())))
    print("{} punctuation letters".format(sum(1 for c in text if c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")))
    print("{} spaces".format(sum(1 for c in text if c.isspace())))
    print("{} digits".format(sum(1 for c in text if c.isnumeric())))

def main() -> None:
    if len(sys.argv) > 2:
        return print("AssertionError : more than one argument")
    if len(sys.argv) == 2:
        return count_print(sys.argv[1])
    print("What is the text to count?")
    return count_print(input()+" ")

if __name__ == "__main__":
    main()