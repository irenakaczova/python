import functools

def debug(func):
    """Print name, args, kwargs and result of decorated function."""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        return_value = func(*args, **kwargs)
        arguments = []
        for arg in args:
            arguments.append(repr(arg))

        for key, val in kwargs.items():
            arguments.append(f"{key}={repr(val)}")

        arguments = ", ".join(arguments)
        
        print(f"Calling: {func.__name__}({arguments})\nResult: {repr(return_value)}")

        return return_value

    return wrapper_debug