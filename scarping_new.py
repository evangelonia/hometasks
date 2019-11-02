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

def filter_parent(pid=0):
    list_of_parent = []
    for p in menu:
        if p.get('pid') == str(pid):
            list_of_parent.append(p)
    return list_of_parent

def print_li(dict1, lvl=0):
    pr_li = ""
    pr_li += f"""\t<li><a href="{dict1["lnk"]}"> {dict1['name']} </a>"""
    pr_li += print_ul(dict1['id'], lvl)
    pr_li += "</li>\n"
    return pr_li




def print_ul(pid, lvl):
    pr_ul = ""
    deti = filter_parent(pid)
    if len(deti) > 0:
        pr_ul += f"\n<ul class='level{lvl + 1}'>"
        for i in deti:
            pr_ul += print_li(i, lvl + 1)
        pr_ul += "</ul>\n"
    return pr_ul


if __name__ == "__main__":

    read_in_list("leftmenu.csv")
    print(menu)

    mnu = print_ul(0, 0)
    print(mnu)
