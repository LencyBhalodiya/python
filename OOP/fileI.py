f = open('sample.txt','r')
data = f.read()
print(data)
f.close()

f = open('sample.txt')
# read first line
data = f.readline() 
print(data)

# Read second line
data = f.readline() 
print(data)

# Read third line
data = f.readline() 
print(data)
f.close()

f = open('another.txt', 'w')
f.write("I am writing ") 
f.write("I am writing") 

with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)