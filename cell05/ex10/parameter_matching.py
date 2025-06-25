def parameter_matching(parameters):
    if len(parameters) != 1:
        print("none")
    else:
        parameter = parameters[0]
        
        while True:
            user_input = input("What was the parameter? ")
            
            if user_input == parameter:
                print("Good job!")
                break
            else:
                print("Nope, sorry...")

if __name__ == "__main__":
    parameter_matching([])
    
    print("'Hello'")
    parameter_matching(["Hello"])
