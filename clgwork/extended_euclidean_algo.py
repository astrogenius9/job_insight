def extended(a,b):
    if a == 0:
        return b, 0, 1

    else:
        gcd, x, y = extended(b % a, a)
        return gcd, y - (b//a) * x, x


def compute(a,b):
    return extended(a, b)

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

gcd, x, y = extended(a,b)

print(f"Value of x = {x} and y = {y}")
print(f"{a}*{x} + {b}*{y} = {gcd}")