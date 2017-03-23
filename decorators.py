import time
import json


def log_duration(fun):
    def wrapper():
        start = time.time()
        fun()
        end = time.time()
        print(end-start)
    return wrapper


def to_json(fun):
    def wrapper():
        result = fun()
        if type(result) is dict:
            new = json.dumps(result)
            print(new)
            return new
        return result
    return wrapper


def ignore_exceptions(excepction_class):
    def ignore(fun):
        def wrapper():
            try:
                fun()
            except excepction_class:
                pass
                return None
        return wrapper
    return ignore




@log_duration
@to_json
@ignore_exceptions(ZeroDivisionError)
def something():
    dict = {}
    for i in range(pow(3,2)):
        i **= 2
        dict.update({i:'hi'})
    print(i)
    1 / 0
    print(dict)
    return dict


something()
