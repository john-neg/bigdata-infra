#!/usr/bin/env python3
import sys
import csv

VALUE_POSITION = 9


def read_input():
    data = csv.reader(sys.stdin.readlines(), dialect=csv.unix_dialect)
    for line in data:
        yield line


def main():
    current_sum, current_count = 0, 0
    for line in read_input():
        try:
            current_sum += int(line[VALUE_POSITION])
            current_count += 1
        except ValueError:
            pass
    print("%s %s" % (current_count, current_sum))


if __name__ == "__main__":
    main()
