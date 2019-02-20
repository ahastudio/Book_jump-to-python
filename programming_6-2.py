# 6-2

# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다.
# 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

def make_multiples(num1, num2, upper_bound):
    result = []
    i = 1
    while i < upper_bound:
        if i % num1 == 0 or i % num2 == 0:
            result.append(i)
        i += 1
    return result

value = sum(make_multiples(3, 5, 1000))
print(value)
