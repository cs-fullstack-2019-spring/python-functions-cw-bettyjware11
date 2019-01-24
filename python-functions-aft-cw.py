def main():
    #Problem1()
    #Problem2()
    #Problem3()
    Problem4()
#Create a function in your program that counts from 0 to [NUMBER]
def Problem1():
    NUMBER = input("Enter number")
    for x in range(0,int(NUMBER)):
        print(x)

#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def Problem2():
    userInput = ""
    while(userInput != 'q'):
        userInput = input("Enter another string")

#Create 4 functions called add, subtract, multiply, and divide. Create them to allow a user
# to perform the name of the function to the two numbers and return the result.
def Problem3():
    x = 3
    y = 6
    addFunction(x,y)
    subtractFunction(x,y)
    multiplyFunction(x,y)
    divideFunction(x,y)

def addFunction(x,y):
    print(x + y)

def subtractFunction(x,y):
    print(x - y)

def multiplyFunction(x,y):
    print(x * y )

def divideFunction(x, y):
    print(x / y)


# Problem3()

#Create a function that will ask the user for a number.
# Use the function to get two numbers, then pass the two numbers
# to a function and ask a user if they want to add, subtract, multiple,
# or divide them. Return a string that prints the two numbers,
# which operation it did, and the result.
def Problem4():
    num1 = int(input("Enter a number"))
    num2 = int(input("Enter a number"))
    whatToDoFunction()


def whatToDoFunction():
    whatToDo = input("Do you want to add, subtract, multiply or divide the numbers?")
    print("num1","num2")

    if(whatToDo == "add"):
        print(f"num1,num2, 'add',num1 + num2")

    elif(whatToDo == "subtract"):
        print(f"num1,num2, 'subtract',num1 -num2")
    elif(whatToDo == "multiply"):
        print(f"num1,num2, 'multiply',num1 * num2")
    elif(whatToDo == "divide"):
        print(f"num1,num2, 'divide', num1 / num2")



if __name__ == '__main__':
    main()
