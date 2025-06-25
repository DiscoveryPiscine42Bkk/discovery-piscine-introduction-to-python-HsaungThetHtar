def string_are_arrays(parameters):
    if len(parameters) != 1:
        print("none")
    else:
        string = parameters[0]
        z_count = 0
        
        for char in string:
            if char == 'z':
                z_count += 1
        
        if z_count == 0:
            print("none")
        else:
            print("z" * z_count)

if __name__ == "__main__":

    string_are_arrays([])
    
    string_are_arrays(["The character Z is not found in this string"])

    string_are_arrays(["The character z is found in this string"])

    string_are_arrays(["Zaz visits the zoo with Zazie"])
