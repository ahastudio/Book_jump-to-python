# 4-2 문제 4
finished = False

while not finished:
    raw_input = input("2부터 9까지의 숫자 중 하나를 입력하세요:")

    sample = '23456789'
    if raw_input not in sample:
        continue

    input = int(raw_input)
    for i in range(1, 10):
        print(input * i, end = ' ')
    break
 
