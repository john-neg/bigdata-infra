#!/usr/bin/env python3
import sys


def read_mapper_output(data):
    for line in data:
        yield line.rstrip().split()


def reduce_variance(count1, mean1, var1, count2, mean2, var2):
    total_count = count1 + count2
    total_mean = (mean1 * count1 + mean2 * count2) / total_count
    if not var1 or not var2:
        total_var = var1 + var2
    else:
        total_var = (count1 * var1 + count2 * var2) / total_count + (
            count1 * count2 * ((mean2 - mean1) / total_count) ** 2
        )
    return total_count, total_mean, total_var


def main():
    total_count, total_mean, total_variance = 0, 0, 0
    for line in read_mapper_output(sys.stdin):
        try:
            current_count = int(line[0])
            current_mean = float(line[1])
            current_variance = float(line[2])
            total_count, total_mean, total_variance = reduce_variance(
                total_count,
                total_mean,
                total_variance,
                current_count,
                current_mean,
                current_variance,
            )
        except ValueError:
            pass
    print(total_variance)


if __name__ == "__main__":
    main()
