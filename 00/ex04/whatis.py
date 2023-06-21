import sys

if len(sys.argv)==2:
    try:
        integer = int(sys.argv[1])
        if integer % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except Exception as e:
        print("AssertionError: argument is not an integer")

if len(sys.argv) > 2:
    print("AssertinError: more than one argument is provided")