from sys import maxsize
from methods.fixed_point import fixed_point


def newton_raphson(f, df, pn, toll=0, max_iter=maxsize):
    return fixed_point(f, pn, toll, max_iter, lambda x: 1 / df(x))


if __name__ == "__main__":
    # sacado del ej. 12 de la guia 2.
    def f(x):
        return (x ** 3) - 9 * (x ** 2) + 24 * x - 20

    def df(x):
        return 3 * (x ** 2) - 18 * x + 24

    print("[Success]")
    table = newton_raphson(f, df, 1.5, 10e-4)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return 0

    def df(x):
        return 0

    print("[Failure]")
    table = newton_raphson(f, df, 0, 1)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")
