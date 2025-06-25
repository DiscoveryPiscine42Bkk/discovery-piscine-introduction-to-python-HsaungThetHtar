import re

def scan_it(*args):
    if len(args) != 2:
        print("none")
        return

    keyword, text = args[0], args[1]

    matches = re.findall(re.escape(keyword), text)

    if not matches:
        print("none")
    else:
        print(len(matches))

scan_it()  
scan_it("the") 
scan_it("the", "the quick brown fox jumps over the lazy dog") 
