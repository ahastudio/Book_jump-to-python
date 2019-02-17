# 4-3 Q3
f1 = open("C:/Users/15U560/Desktop/2019-1/python/workspace/pythonbook/abc.txt", 'r')
lines = f1.readlines()
f1.close()

f2 = open("C:/Users/15U560/Desktop/2019-1/python/workspace/pythonbook/abc.txt", 'w')
for i in range(0, len(lines)):
    f2.write(lines[-(1+i)])
f2.close()
