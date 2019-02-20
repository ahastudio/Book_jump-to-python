# 4-1 문제 1

def is_natural_number(n):
    if type(n) == int and n > 0:
        return True

def is_odd(n):
    if not is_natural_number:
        print('자연수를 입력해주십시오')
        return
    
    return n % 2 != 0

n = int(input('자연수를 입력하세요: '))
print('%d = %s' % (n, ['짝수', '홀수'][is_odd(n)]))
