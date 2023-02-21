#!/usr/bin/env python3
import sys


def read_mapper_output(data):
    for line in data:
        yield line.rstrip().split()


def main():
    total_sum, total_count = 0, 0
    for line in read_mapper_output(sys.stdin):
        try:
            current_count, current_sum = line
            total_count += int(current_count)
            total_sum += int(current_sum)
        except ValueError:
            pass
    print(total_sum / total_count)


if __name__ == "__main__":
    main()
