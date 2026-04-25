# def exponent_func(base, power):
#     return base ** power

# print(exponent_func(2, 3))  # Output: 8
def exponent_func(base, power):
    result = 1
    for i in range(power):
        result = result * base
    return result
print(exponent_func(45, 34))  # Output: 8