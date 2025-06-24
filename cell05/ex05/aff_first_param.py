import sys
def para(*args):
    if len(args) == 0:
        print('none')
    else:
        print(f"{args[0]}")

    
para()
para( "Code Ninja", "Numerique", "42")
