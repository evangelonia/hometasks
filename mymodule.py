"""Make a directory with 2 modules,
make a function in one of them, 
then import the function
in the other module and use that in a script of your choosing 
Создайте каталог с двумя модулями, 
сделайте функцию в одном из них,
 затем импортируйте функцию в другой модуль
  и используйте ее в выбранном вами скрипте"""

def make_operation(operator,*nums):
    if len(nums)<1:
        return 0
    ret = nums[0]
    for n in nums[1:]:
        if operator == "+":
            ret += n
        elif operator == "-":
            ret -= n
        elif operator == "*":
            ret *= n
    return ret

#rez = make_operation("+",7, 7, 2)


#print(rez)