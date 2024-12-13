def calculate_structure_sum( *args):
    counter = 0
    for i in args:
        # print(i)
        # print(isinstance(i, int))
        if isinstance(i, int) or isinstance(i, float):
            counter += i
        elif isinstance(i,list) or isinstance(i, set) or isinstance(i, tuple):
            counter += calculate_structure_sum(*i)
        elif isinstance(i, str):
            # print(len(i))
            counter += len(i)
        elif isinstance(i, dict):
            counter += calculate_structure_sum(*i.keys())
            counter += calculate_structure_sum(*i.values())
    return counter

# data_structure = [1, 2.5, [1, 1], 'a']
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)
print(result)