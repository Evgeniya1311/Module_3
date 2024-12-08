def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 10)
print_params(True, c=5)
print_params(b = 25)
print_params(c = [1,2,3])

print()
values_list = [428, False, 'Mamba']
values_dict = {'a': 89, 'b': True, 'c': 'Chelny'}

print_params(*values_list)
print_params(**values_dict)

print()
values_list_2 = ['Kazan', 564]
print_params(*values_list_2, 42)

