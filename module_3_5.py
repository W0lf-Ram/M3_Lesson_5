def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1 and first != 0:
        return first
    if first == 0:
        return 1
    else:
        result = first * get_multiplied_digits(int(str_number[1:]))
        return result

result = get_multiplied_digits(40580)
print(result)

