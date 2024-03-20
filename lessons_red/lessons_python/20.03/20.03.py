file_name = "answer.txt"

file = open(file_name,"r",encoding="utf-8")
content = file.read()
print(content)
file.close()