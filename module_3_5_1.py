def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    # print('first is ', first)
    if len(str_number[1:]) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print('Результат рекурсивного умножения:',get_multiplied_digits(41021))
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)