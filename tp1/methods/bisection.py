from sys import maxsize


def bisection(f, a, b, toll=0, max_iter=maxsize):
    ps = []

    for n in range(0, max_iter):
        pn = (a + b) / 2
        fpn = f(pn)

        ps.append((n, pn, fpn))
        if abs(fpn) <= toll:
            break

        if f(a) * fpn > 0:
            a = pn
        else:
            b = pn

    return ps


if __name__ == "__main__":
    from math import sin, cos, exp

    # sacado del ej. 1 de la guia 2.
    def f(x):
        return exp(x) * (sin(x) + cos(x) - 2 * x - 2)

    print("[Success]")
    table = bisection(f, -2.5, -0.5, 10e-5)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")

    def f(x):
        return 0

    print("[Failure]")
    table = bisection(f, -1, 4, max_iter=100)
    print(f"found x = {table[-1][1]} with f(x) = {f(table[-1][1])}")
