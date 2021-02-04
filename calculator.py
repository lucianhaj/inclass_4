def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):

    return int(a) - int(b)


def division(a, b):
    try:
        float(a) / float(b)
    except ZeroDivisionError:
        return "error: divide by zero"
    else:
        return float(a) / float(b)


def multiplication(a, b):

    return float(a) * float(b)


