# 4-1 문제 2

def ave_all(*args):
    sum = 0
    for i in args: sum += i
    result = sum / len(args)
    return result
