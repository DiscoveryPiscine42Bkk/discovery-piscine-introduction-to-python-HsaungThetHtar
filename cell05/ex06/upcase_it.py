#!/usr/bin/env python3

import sys   
if len(sys.argv) <= 1:
    print("none")
else:
    parameter = sys.argv

    for i in parameter[1::]:
        print(i.upper(),end=" ")
        



    
    

