import urllib.request
import webbrowser

'''Напишите программу, которая использует urllib.request для открытия данного URL. Например, 
если вы запустите программу и введете https://www.google.com/, программа откроет URL-адрес в веб-браузере.'''


def open_url(url):
    i = urllib.request.urlopen(url)
    return webbrowser.open(url)

open_url("https://www.google.com/")







