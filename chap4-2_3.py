# 4-2 문제 4
end_bool = False

while end_bool == False:
    raw_input = input("2부터 9까지의 숫자 중 하나를 입력하세요:")

    sample1 = ['2', '3', '4', '5', '6', '7', '8', '9']
    if raw_input not in sample1:
        continue

    input = int(raw_input)
    for i in range(1,10):
        print(input*i, end = ' ')

    end_bool = True
