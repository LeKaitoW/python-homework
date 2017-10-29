import time
import json


def log_duration(fun):
    def wrapper():
        start = time.time()
        fun()
        end = time.time()
        print('log time = ', end-start)
    return wrapper


def to_json(fun):
    def wrapper():
        result = fun()
        if type(result) is dict:
            new = json.dumps(result)
            return new
        return result
    return wrapper


def ignore_exceptions(exception_class):
    def ignore(fun):
        def wrapper():
            try:
                fun()
            except exception_class:
                pass
                return None
        return wrapper
    return ignore


#@log_duration
#@to_json
#@ignore_exceptions(ZeroDivisionError)
def something():
    dict = {}
    for i in range(pow(3,2)):
        i **= 2
        dict.update({i:'hi'})
    #1 / 0
    return dict


print('finally: ', something())
