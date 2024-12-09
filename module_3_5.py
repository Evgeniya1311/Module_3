def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    #print('first is ', first)
    if len(str_number[1:]) > 0:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


print('Результат рекурсивного умножения:',get_multiplied_digits(41021))