import functools


def filter_age(func):
    @functools.wraps(func)
    def wrapper_filter_age(*args, **kwargs):
        # print('ARGS', args)
        print('KWARGS', kwargs)
        print('KWARGS', *kwargs)
        print('KWARGS', **kwargs)
        return func(*args, **kwargs)
    return wrapper_filter_age


@filter_age
def go_to_bar(age, name):
    if age < 21:
        print(f'You are not allowed! {name}')
    else:
        print(f'Welcome {name}')


go_to_bar(18, name='Amar')