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
        if p.get(pid):
            list_of_parent.append(p)
    return list_of_parent


def print_li(dict1, lvl=0):
    # вывели открывающуюся лишку
    pr_li = f"""\t<li>{dict1["name"]}"""
    pr_li += f"""\t<li><a>{dict1["lnk"]}"""
    pr_li += "</a>\n"
    # Выведем если есть дети
    pr_li += print_ul(dict1['id'], lvl)
    # закрыли лишку
    pr_li += "</li>\n"
    pr_li += "</li>\n"

    return pr_li


def print_ul(pid, lvl):
    pr_ul = ""
    # получили детей
    deti = filter_parent(pid)
    # если есть дети
    if len(deti) > 0:
        # открыли улку
        pr_ul += f"\n<ul class='level{lvl + 1}'>"
        # в цикле по детям вызвали вывод их лишки
        for i in deti:
            pr_ul += print_li(i, lvl + 1)
        # закрыли улку
        pr_ul += "</ul>\n"
    # вернули собранный текст
    return pr_ul


if __name__ == "__main__":

    # прочитали в переменную
    read_in_list("leftmenu.csv")
    print(menu)
    # print(filter_parent(4))

    # Вводим нулевой уровень
    mnu = print_ul(0, 0)
    print(mnu)