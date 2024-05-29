import time
from functools import wraps

class Throttler:
    """
    A class to enforce rate limiting on function calls.

    Attributes:
        rate_limit (int): The maximum number of allowed calls within the period.
        period (int): The time period in seconds during which the rate limit applies.
        last_call (float): The time of the last function call.
        num_calls (int): The number of calls made within the current period.
    """
    
    def __init__(self, rate_limit: int, period: int):
        """
        Initialize the Throttler with a rate limit and a period.

        Args:
            rate_limit (int): The maximum number of allowed calls within the period.
            period (int): The time period in seconds during which the rate limit applies.
        """
        self.rate_limit = rate_limit
        self.period = period
        self.last_call = 0
        self.num_calls = 0

    def throttle(self):
        """
        Enforce the rate limit. If the number of calls exceeds the rate limit within the period, this method will make the calling thread sleep until the period resets.
        """
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

    Args:
        rate_limit (int): The maximum number of allowed calls within the period.
        period (int): The time period in seconds during which the rate limit applies.

    Returns:
        cls: The decorated class with throttling applied to its methods.
    """
    def decorator(cls):
        """
        Decorate the class by wrapping its methods with throttling.

        Args:
            cls: The class to decorate.

        Returns:
            cls: The decorated class with throttling applied to its methods.
        """
        throttler = Throttler(rate_limit, period)
        
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                wrapped_attr = wrap_with_throttle(attr, throttler)
                setattr(cls, attr_name, wrapped_attr)
        
        return cls

    def wrap_with_throttle(func, throttler):
        """
        Wrap a function with throttling.

        Args:
            func: The function to wrap.
            throttler: The Throttler instance to use for throttling.

        Returns:
            func: The wrapped function with throttling applied.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            throttler.throttle()
            return func(*args, **kwargs)
        return wrapper

    return decorator