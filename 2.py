data = [1, 3, 2, 17, 20, 6, 7, 22, 99, 10, 'c', 'b', 'a', 'd', 'e', 'g', 'f', 'z', 'h', 'i']
ints = sorted(x for x in data if type(x) is int)
strs = sorted(x for x in data if type(x) is str)
list = ints + strs
even_numbers = [x for x in ints if x % 2 == 0]
caps = [x.upper() for x in strs]
print('Відсортований список : ',list)
print('Парні числа: ', even_numbers)
print('Капсом: ', caps)

