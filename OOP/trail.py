with open('sample.txt') as f:
    content = f.read()

content = content.replace("lency","Mr.Boss")

with open("sample.txt", "w") as f:
     f.write(content)