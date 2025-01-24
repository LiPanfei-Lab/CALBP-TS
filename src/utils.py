import json
import time
from functools import wraps


def load_json(file_name):
    with open(file_name, 'r') as f:
        lines = f.read()
        data = json.loads(
            lines, object_hook=lambda d: {int(k) if k.lstrip('-').isdigit() else k: v for k, v in d.items()})
    return data


def save_json(json_data, file_name):
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_data, sort_keys=True, indent=4))


def time_it(module=None, logger=None):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            s_t = time.time()
            res = func(*args, *kwargs)
            e_t = time.time()
            m = module
            if m is None:
                m = func.__name__
            print("{0} time cost: {1}s".format(m, e_t - s_t))
            if logger is not None:
                logger.info("{0} time cost: {1}s".format(m, e_t - s_t))
            return res
        return wrapper
    return inner
