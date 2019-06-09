#!/usr/bin/env python3

import sys
import string
import filecmp

original = open(sys.argv[1])
sent = open(sys.argv[2])
result = open(sys.argv[3])

indomain = True
counter = 0
byte = sent.read(1)
while byte:
	if byte not in string.ascii_uppercase + string.digits + string.whitespace:
		indomain = False
	counter += 1
	byte = sent.read(1)

if not indomain:
	sys.exit(1)

counter2 = 0
byte = original.read(1)
while byte:
	counter2 += 1
	byte = sent.read(1)

print("Increment ", end='')
print(float(counter2)/float(counter))

result_line = result.readlines()
result_line = result_line[0].strip()
if (filecmp.cmp(sys.argv[1], sys.argv[2]) and result_line == 'OK') or \
 (not filecmp.cmp(sys.argv[1], sys.argv[2]) and result_line == 'KO'):
	sys.exit(0)
else:
	sys.exit(1)
