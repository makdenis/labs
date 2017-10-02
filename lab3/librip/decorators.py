

import functools

def print_result_helper(func, res):
    print(func.__name__)
    tp = type(res).__name__
    if tp == 'list':
        [print(i) for i in res]
    elif tp == 'dict':
        [print('{0}={1}'.format(k,v)) for k,v in res.items()]
    else:
        print(res)


def print_result(func):
    #@functools.wraps(func)
    def decorated_func(*args,**kwargs):
        res = func(*args,**kwargs)
        print_result_helper(func, res)
        return res
    return decorated_func
