def power(x, y):
    result = 1

    if y==0:
        return 1

    else:
        while y > 0:
            result = result * x
            y = y - 1

    return result


a=int(input('Enter Base: '))
b=int(input('Enter Exponent: '))
print(power(a,b))
