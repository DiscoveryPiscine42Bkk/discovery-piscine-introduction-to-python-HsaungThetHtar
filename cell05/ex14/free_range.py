def free_range(parameters):
    if len(parameters) != 2:
        print("none")
    else:
        start = int(parameters[0])
        end = int(parameters[1])
        
        array = list(range(start, end + 1))
        print(array)

if __name__ == "__main__":
    free_range([])
    free_range(["10", "14"])
