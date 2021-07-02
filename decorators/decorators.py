# Can not accept any arguments as parameter

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice



# Accepts any number of arguments as paramter
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice  