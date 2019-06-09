#!/usr/bin/env python3

"""Computes mean value"""

def mean(input_file):
    """Computes mean value of integers in input_file"""
    increment_accum = 0.0
    ok_accum = 0
    counter = 0
    for line in input_file:
        if len(line.split()) != 2:
            print("Error in mean: " + line)
        increment, ok = line.split()
        increment_accum += float(increment)
        if ok == 'OK':
            ok_accum += 1
        counter += 1

    if counter == 0:
        print(0)
    else:
        print("{:.2f}".format(increment_accum/counter) + ' ' + str(ok_accum/counter) )

if __name__ == "__main__":
    import sys
    mean(sys.stdin)
