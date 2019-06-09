#!/usr/bin/env python3

"""Check correctness of assignment"""

import sys
import string

def main():
    """Check correctness of assignment"""
    original = open(sys.argv[1])
    sent = open(sys.argv[2])
    noisy = open(sys.argv[3])
    result = open(sys.argv[4])

    indomain = True
    counter = 0
    byte = sent.read(1)
    byte_noisy = noisy.read(1)
    files_different = -1
    while byte:
        if byte not in string.ascii_uppercase + string.digits + string.whitespace:
            indomain = False
        if byte != byte_noisy:
            files_different = counter
        counter += 1
        byte = sent.read(1)
        byte_noisy = noisy.read(1)
    if not indomain:
        print("Not in domain")
        sys.exit(1)

    counter2 = 0
    byte = original.read(1)
    while byte:
        counter2 += 1
        byte = original.read(1)
    print("Increment ", end='')
    print(float(counter)/float(counter2), end='')

    result_line = result.readlines()
    result_line = result_line[0].strip()
    print(' ' + result_line)
    if files_different < 0:
        if result_line == 'OK':
            sys.exit(0)
        else:
            print('Detection error: sent file not modified')
            sys.exit(1)
    else:
        if result_line == 'KO':
            sys.exit(0)
        else:
            print('Detection error: sent file has been modified in byte ' + str(files_different))
            sys.exit(1)

if __name__ == "__main__":
    main()
