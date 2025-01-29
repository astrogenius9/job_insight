def extended(a,b):
    if a == 0:
        return b, 0, 1

    else:
        gcd, x, y = extended(b % a, a)
        return gcd, y - (b//a) * x, x

def diophantine(a,b,c):

    gcd, x, y = extended(a,b)

    if c%gcd != 0:
        raise None

    x *= c // gcd
    y *= c // gcd

    return x, y

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

solution = diophantine(a,b,c)

if solution is None:
    print("No solution")
else:
    x, y = solution
    print(f"Value of x = {x} and y = {y}")
    print(f"{a}*{x} + {b}*{y} = {c}")