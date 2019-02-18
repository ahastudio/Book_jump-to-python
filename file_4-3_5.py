# 4-3 Q5

with open("sample.txt", 'r') as f1:
    raw_data = f1.read()
    data = raw_data.split()
    numbers = [int(i) for i in data]
    sum_result = sum(numbers)
    average = sum_result / len(numbers)

with open("result.txt", 'w') as f2:
    f2.write(str(average))
