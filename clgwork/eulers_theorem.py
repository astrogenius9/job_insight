def euler(a, n):

    def totient(n):
        result = 1

        for i in range(2, n):
            if gcd(i,n) == 1:
                result += 1

        return result

    def gcd(a,b):

        while b!=0:
            a, b = b, a%b

        return a

    phi = totient(n)
    result = pow(a, phi, n)
    return phi, result

a = int(input("Enter a positive integer a: "))
n = int(input("Enter a positive integer n: "))

phi, result = euler(a, n)

if result == 1:
    print(f"{a} ^ {phi} = {result} (mod {n})")
else:
    print("Euler's theorem not true ")
