#!/usr/bin/env python3
import statistics
import sys
import csv

VALUE_POSITION = 9


def read_input():
    data = csv.reader(sys.stdin.readlines(), dialect=csv.unix_dialect)
    values = []
    for line in data:
        try:
            values.append(int(line[VALUE_POSITION]))
        except ValueError:
            pass
    return values


def main():
    values = read_input()
    values_count = len(values)
    values_mean = sum(values) / values_count
    values_variance = statistics.variance(values)
    print("%s %s %s" % (values_count, values_mean, values_variance))


if __name__ == "__main__":
    main()
