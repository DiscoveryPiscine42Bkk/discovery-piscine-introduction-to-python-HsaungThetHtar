def append_it(parameters):
    if len(parameters) == 0:
        print("none")
    else:
        for parameter in parameters:
            if not parameter.endswith("ism"):
                print(parameter + "ism")

if __name__ == "__main__":
    append_it([])
    append_it(["parallel", "egoism", "human"])
