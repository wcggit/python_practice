def f(*args, **kwargs):
    return sum(args[0])


def f2(x, y, z):
    return x + y + z


def passFunction(f):
    def g(x):
        return f(x)

    return g


if __name__ == '__main__':
    g = passFunction(f)
    print g((1,2))
