import functools
import time

def delay(seconds=1):
    """Delays the runtime of the decorated function for X seconds"""
    
    def decorator_delay(func):
        @functools.wraps(func)
        def wrapper_delay(*args, **kwargs):
            time.sleep(seconds)
            value = func(*args, **kwargs)
            return value
        return wrapper_delay
    return decorator_delay