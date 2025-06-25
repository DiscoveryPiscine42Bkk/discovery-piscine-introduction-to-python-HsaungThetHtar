
def downcase_it(string):
    return string.lower()

def downcase_all(parameters):
    if len(parameters) == 0:
        print("none")
    else:
        for parameter in parameters:
            print(downcase_it(parameter))


downcase_all([])

downcase_all(["HELLO WORLD", "I understood Arrays well!"])
