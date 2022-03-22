def compare(a, b):
    if a > b:
        return a, b
    else:
        return b, a


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
compare(a, b)
print()
print(f"GCD of {a} & {b} is:  {gcd(a, b)}")
