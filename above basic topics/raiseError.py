def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")

a = increment('df364')
print(a)

try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successful") #prints only if the their is no error or exceptions

try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done") #always prints regardless of the error

print("Thanks for using the program")