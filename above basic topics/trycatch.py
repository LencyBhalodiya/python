while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a number greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this game")

try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
    
except ValueError as e:
    print("Please Enter a valid value") 

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")