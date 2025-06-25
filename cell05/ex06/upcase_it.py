import sys
def para(*args):
    if len(args) == 0:
        print("none")
    else:
        for i in range(len(args)):
            a = args[i].upper()
            print(f"{a}", end=" ")
        print()  

para()
para("initiation")
para('This exercise is quite easy!')
