#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        result = None
        return result
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
