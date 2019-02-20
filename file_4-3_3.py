# 4-3 Q3
f1 = open("./abc.txt", 'r')
lines = f1.readlines()
f1.close()

f2 = open("./abc.txt", 'w')
for line in lines[::-1]:
    f2.write(line)
f2.close()
