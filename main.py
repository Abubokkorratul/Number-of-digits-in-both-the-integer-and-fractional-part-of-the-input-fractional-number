num = input("Enter a fractional number: ")
if '.' in num:
    integer_part, fractional_part = num.split('.')
    print("Number of digits in integer part:", len(integer_part))
    print("Number of digits in fractional part:", len(fractional_part))
else:
    print("The input has no fractional part. Digits in integer part:", len(num))
