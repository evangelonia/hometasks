import os
import csv

menu = []

def read_in_list(filename):
    if os.path.exists(filename):
        with open(filename, encoding="utf-8") as fn:
            spamreader = csv.DictReader(fn)
            for line in spamreader:
                menu.append(dict(line))
    else:
        raise FileNotFoundError
        
        
 def filter_parent(pid):
    list_of_parent = []
    for p in menu:
        if p.get("parent") == str(pid):
            list_of_parent.append(p)
    return list_of_parent

if __name__ == "__main__":
    read_in_list("exmpl.csv")
    print(menu)
