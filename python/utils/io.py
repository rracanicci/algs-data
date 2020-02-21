
def display_result(func, *args, **kargs) -> None:
    print (f"{func.__name__}: {func(*args, **kargs)}")

def read_file(path: str, encoding: str ='UTF-8') -> str:
    with open(path, 'rb') as f:
        return f.read().decode(encoding)
    return None