# 4-2 문제 2

input = input("숫자를 콤마로 구분하여 입력하세요:")
numbers = input.split(",")
for i in range(0,len(numbers)):
    numbers[i] = int(numbers[i])
sum = 0
for j in range(0,len(numbers)):
    sum += numbers[j]
print("숫자들의 총합은 %d 입니다" % sum)
