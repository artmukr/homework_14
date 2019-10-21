from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(value):
        def decorator(*args):
            return int(value(*args))
        return decorator

    @staticmethod
    def to_str(value):
        def decorator(*args):
            return str(value(*args))
        return decorator

    @staticmethod
    def to_bool(value):
        def decorator(*args):
            return bool(value(*args))
        return decorator

    @staticmethod
    def to_float(value):
        def decorator(*args):
            return float(value(*args))
        return decorator


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
