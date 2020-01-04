def check_result(func):
    def wrapper(*args):
        for input_, target_ in zip(*args):
            output = func(input_)
            assert output == target_, f'expected f({input_})={target_}, got-> {output}'
        return

    return wrapper
