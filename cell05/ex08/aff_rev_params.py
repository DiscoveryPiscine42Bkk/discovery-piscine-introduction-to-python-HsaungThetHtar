def para(args=None):
    if args is None:
        args = []

    if len(args) < 2:
        print("none")
    else:
        for arg in reversed(args):
            print(arg)

para()
para(["coucou"])
para(["Python", "piscine", "hello"])
