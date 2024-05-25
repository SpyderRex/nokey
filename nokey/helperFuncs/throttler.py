import time
from functools import wraps

class Throttler:
    def __init__(self, rate_limit: int, period: int):
        self.rate_limit = rate_limit
        self.period = period
        self.last_call = 0
        self.num_calls = 0

    def throttle(self):
        current_time = time.time()
        elapsed = current_time - self.last_call

        if elapsed >= self.period:
            self.last_call = current_time
            self.num_calls = 0

        if self.num_calls >= self.rate_limit:
            sleep_time = self.period - elapsed
            print(f"Rate limit reached. Sleeping for {sleep_time:.2f} seconds.")
            time.sleep(sleep_time)
            self.last_call = time.time()
            self.num_calls = 0

        self.num_calls += 1
        
        


def throttle_class(rate_limit: int, period: int):
    """
    Class decorator to apply throttling to all methods in the class.
    """
    def decorator(cls):
        throttler = Throttler(rate_limit, period)
        
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                wrapped_attr = wrap_with_throttle(attr, throttler)
                setattr(cls, attr_name, wrapped_attr)
        
        return cls

    def wrap_with_throttle(func, throttler):
        @wraps(func)
        def wrapper(*args, **kwargs):
            throttler.throttle()
            return func(*args, **kwargs)
        return wrapper

    return decorator