import os

def find_str_file(dir, s):
    if s in os.path.split(dir)[1]:
        print(os.path.relpath(dir))
    if os.path.isfile(dir):
        return

    for x in os.listdir(dir):
        find_str_file(os.path.join(dir, x), s)

find_str_file('.', 'o')
