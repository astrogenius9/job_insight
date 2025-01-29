def fermats(a,p):

    if not is_prime(p):
        raise ValueError("Not a prime number. ")

    result = pow(a,p-1,p)
    return result

def is_prime(n):

    if n<=1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    max = int(n**0.5) + 1
    for i in range(3, max, 2):
        if n%i == 0:
            return False

    return True

a = int(input("Enter a positive integer: "))
p = int(input("Enter a prime number: "))

result = fermats(a,p)

print(f"{a} ^ {p-1} = {result} (mod {p})")

