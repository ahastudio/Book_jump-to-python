# 4-3 Q4

with open("./test.txt", 'r') as f:
    data = f.read()
    
converted = data.replace('java', 'python')
    
with open("./test.txt", 'w') as f:
    f.write(converted)
    
    
# TEXT_FILE_PATH = "./test.txt"

# def read_file():
#     with open(TEXT_FILE_PATH, 'r') as f:
#         return f.read()
    
# def write_file(text):
#     with open(TEXT_FILE_PATH, 'w') as f:
#         f.write(text)
        
# text = read_file()
# write_file(text.replace('java', 'python'))
