# 4-3 Q4

with open("C:/Users/15U560/Desktop/2019-1/python/workspace/pythonbook/test.txt", 'r') as f1:
    whole_data = f1.read()
    each_data = whole_data.split(' ')
    each_data[-1] = "python"

with open("C:/Users/15U560/Desktop/2019-1/python/workspace/pythonbook/test.txt", 'w') as f2:
    new_data = ' '.join(each_data)
    f2.write(new_data)
