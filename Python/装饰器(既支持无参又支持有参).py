from typing import Callable, Any


def log(func_or_arg: Any):
    # 函数情况
    if isinstance(func_or_arg, Callable):
        def wrapper(*args, **kwargs):
            func_name = func_or_arg.__name__
            print("func: %s, starting..." % func_name)
            f = func_or_arg(*args, **kwargs)
            print("func: %s, ending..." % func_name)
    # 其余情况
    else:
        def wrapper(func: Callable):
            def inner_wrapper(*args, **kwargs):
                func_name = func.__name__
                print("func: %s, %s..." % (func_name, func_or_arg))
                f = func(*args, **kwargs)
                print("func: %s, %s..." % (func_name, func_or_arg))
                return f
            return inner_wrapper
    # 返回装饰器函数
    return wrapper
