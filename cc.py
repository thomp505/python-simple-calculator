def add(x, y):
    return x+y;

def subtract(x, y):
    return x-y;

def multiply(x, y):
    return x*y;

def divide(x,y):
    return x/y ;
print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Kill")

while True:

    choice=input("Select 1/2/3/4/5 : ")

    if choice in ('1','2','3','4'):
        num1=float(input("Enter 1st number: "))
        num2=float(input("Enter 2nd number: "))

    if choice == '1':
        print(num1, '+', num2, '=', add(num1,num2))
    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1,num2))
    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1,num2))
    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1,num2))
    elif choice == '5':
        print("You ended the program")
        break
    
else:
    print("Invalid Input")
