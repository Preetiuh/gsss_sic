def my_range(*var_args):
    if len(var_args) < 1 or len(var_args) > 3:
        print('TypeError. You gave either 0 or more than 3 Args')
    elif len(var_args) == 1:
        i = 0
        while i < var_args[0]:
            yield i
            i += 1
    elif len(var_args) == 2:
        i = var_args[0]
        while i < var_args[1]:
            yield i
            i += 1
    elif len(var_args) == 3:
        start, stop, step = var_args
        if step == 0:
            print("ValueError: step must not be zero")
            return
        if start < stop and step > 0:
            i = start
            while i < stop:
                yield i
                i += step
        elif start > stop and step < 0:
            i = start
            while i > stop:
                yield i
                i += step
        else:
            return
    else:
        print('invalid input')

