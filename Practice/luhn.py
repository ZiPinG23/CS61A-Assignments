def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10 :
        return n
    else:
        all_but_last , last = split(n)
        return sum_digits(all_but_last) + last

def luhn_num(n):
    if n < 10:
        return n
    else:
        all_but_last , last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digits = sum_digits(2*last)
    if n < 10:
        return luhn_digits
    else:
        return luhn_num(all_but_last) + luhn_digits



print(luhn_num(4505470044242151))