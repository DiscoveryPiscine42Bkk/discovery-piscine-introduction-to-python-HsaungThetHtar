def count_it(parameters):
    if len(parameters) == 0:
        print("none")
    else:
        print(f"parameters: {len(parameters)}")
        
        for parameter in parameters:
            print(f"{parameter}: {len(parameter)}")

if __name__ == "__main__":
    count_it([])
    count_it(["Game", "of", "Thrones"])
