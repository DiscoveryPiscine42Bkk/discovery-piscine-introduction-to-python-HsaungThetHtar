#!/usr/bin/env python3

def array_of_names(dictionary):
    names_array = []
    for first_name, last_name in dictionary.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        names_array.append(full_name)
    return names_array

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))