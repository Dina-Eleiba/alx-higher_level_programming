#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv)
    if number == 1:
        print("{} arguments.".format(number - 1))
    elif number == 2:
        print("{} argument:".format(number - 1))
        print("{}: {}".format(number - 1, sys.argv[number - 1]))
    else:
        print("{} arguments:".format(number - 1))
        for i in range(1, number):
            print("{}: {}".format(i, sys.argv[i]))
