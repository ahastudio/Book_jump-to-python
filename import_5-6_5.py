# 5-6 Q5
import random
def random_pop(subject):
    result = []
    for i in range(6):
        removal = random.choice(subject) # 무작위 추첨
        subject.remove(removal) # 원래 list에서 없애고,
        result.append(removal) # 그 없앤 걸 출력할 리스트에 추가
    return result

numbers = list(range(1,46)) # 1~45 list
lotto = random_pop(numbers)
print(lotto) # 출력
    
