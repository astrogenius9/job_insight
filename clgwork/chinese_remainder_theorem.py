def crt(n, a):
    def extended(a, b):
        if a == 0:
            return b, 0, 1

        else:
            gcd, x, y = extended(b % a, a)
            return gcd, y - (b // a) * x, x

    def inv(a,m):

        gcd, x, y = extended(a,m)
        if gcd!=1:
            raise ValueError("Solution isnt there")

        return x % m

    N = 1
    for ni in n:
        N *= ni

    x = 0
    for ai, ni in zip(a,n):
        Mi = N//ni
        x += ai*Mi*inv(Mi, ni)

    return x % N

n = []
a = []
i = int(input("Enter number of linear congruences: "))
while (i>0):
    a1 = int(input("Enter number for a: "))
    a.append(a1)
    n1 = int(input("Enter number for n: "))
    n.append(n1)
    i=i-1

x = crt(n,a)
print("The solution to the system of congruences is:", x)


