from contextlib      import contextmanager
from time            import time

@contextmanager
def timeit(description: str) -> None:
    start = time()
    yield
    ellapsed_time = (time() - start) * 1000
    print (f"{description} [{ellapsed_time:.2f} ms]")

def timeit_run(func, *args, **kargs) -> None:
    with timeit(func.__name__):
        func(*args, **kargs)