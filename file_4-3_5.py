# 4-3 Q5

with open("sample.txt", 'r') as f:
    numbers = [int(i) for i in f.readlines()]
    
average = sum(numbers) / len(numbers)
    
with open("result.txt", 'w') as f:
    f.write(str(average))
