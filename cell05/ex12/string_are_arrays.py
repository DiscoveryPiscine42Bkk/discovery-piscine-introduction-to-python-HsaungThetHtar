#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    string = sys.argv[1]
    z_count = 0
    
    for char in string:
        if char == 'z':
            z_count += 1
    
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)
