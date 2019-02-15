# 4-1 문제 1

def is_odd(n):
    if type(n) != int:
        print('자연수를 입력해주십시오')
    elif n <= 0:
        print('자연수를 입력해주십시오')
    else:
        if n % 2 == 0:
            print('%d = 짝수' % n)
        else:
            print('%d = 홀수' % n)
