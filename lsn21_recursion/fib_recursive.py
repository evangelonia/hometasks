"""Make a function that takes an integer i as parameter,
then return a list of numbers in the fibonacci
sequence all the way to the ith element in the sequence

Создайте функцию, которая принимает целое число i в качестве параметра,
 а затем возвращает список чисел в последовательности Фибоначчи
 до i-го элемента в последовательности"""

def fib_list(i):
    if i == 0:
        return [0]
    elif i == 1:
        return [0, 1]
    else:
        lst = fib_list(i-1)
        lst.append(lst[-1] + lst[-2])
        return lst

print(fib_list(int(input("До какого элемента?:"))))