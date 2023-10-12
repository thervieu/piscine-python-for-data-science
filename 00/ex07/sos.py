

import sys


def morse_translator():
    """morse_translator() -> None

    Prints the sentence in morse code."""

    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-'}
    try:
        if len(sys.argv) != 2:
            raise Exception("AssertionError : wrong number of arguments")
        p = " !\"#$%&'()*+/:;<=>@[\\]^_`{|}~"
        if sum(1 for c in sys.argv[1] if c in p) != 0:
            raise Exception("AssertionError : string is wrong")
        translation = [MORSE_CODE_DICT[c] for c in sys.argv[1].upper()]
        print(*translation, sep=' ')
    except Exception as e:
        return print(e)


if __name__ == "__main__":
    morse_translator()
