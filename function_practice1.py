# 4-1 문제 1

def is_natural_number(n):
    if type(n) == int and n > 0:
        return True

def is_odd(n):
    if is_natural_number(n) == False:
        print('자연수를 입력해주십시오')
        return
    
    if n % 2 == 0:
        print('%d = 짝수' % n)
    else:
        print('%d = 홀수' % n)
