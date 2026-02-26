def make_polynomial(coeffs):
    """
    coeffs: list like [a_n, a_{n-1}, ..., a_1, a_0]
    returns: function f(x)
    """
    n = len(coeffs) - 1

    def f(x):
        # Evaluate polynomial: a_n x^n + ... + a_0
        total = 0.0
        for i, a in enumerate(coeffs):
            power = n - i
            total += a * (x ** power)
        return total

    return f


def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        return None

    while abs(b - a) > tol:
        c = (a + b) / 2

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# --------- Input from user ----------
deg = int(input("Enter degree of polynomial: "))

print(f"Enter {deg+1} coefficients from highest power to constant:")
coeffs = []
for p in range(deg, -1, -1):
    coeffs.append(float(input(f"Coefficient of x^{p}: ")))

a = float(input("Enter a (lower limit): "))
b = float(input("Enter b (upper limit): "))
tol = float(input("Enter tolerance (e.g. 0.001): "))

f = make_polynomial(coeffs)

root = bisection_method(f, a, b, tol)

if root is None:
    print("Invalid interval: f(a) and f(b) must have opposite signs.")
else:
    print("Root:", root)
    print("f(root):", f(root))