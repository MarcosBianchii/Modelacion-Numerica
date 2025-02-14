from fixed_point import fixed_point


def newton_raphson_modified(f, df, d2f, pn, toll=0, max_iter=1000):
    def psy(xn):
        return df(xn) / (df(xn) ** 2 - f(xn) * d2f(xn))

    return fixed_point(f, pn, toll, max_iter, psy)
