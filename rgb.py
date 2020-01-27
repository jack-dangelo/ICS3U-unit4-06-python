#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: Oct 2019
# This program uses a nested loop


def main():
    # this function uses a nested loop

    red = 0
    green = 0 
    blue = 0 

    # process & output
    for red in range(0, 256):
        for green in range(0, 256):
            for blue in range(0, 256):
                print("RGB ({0}, {1}, {2})".format(red, green, blue))


if __name__ == "__main__":
    main()
