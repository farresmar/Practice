#printing something in a function
def test1():
    print("hi")
test1()

#Saving the return of a function to a variable
def test2():
    return "hello"
x = test2()
print(x)

#function with argument
def test3(x):
    print(x)
test3("howdy")

#calculator function
def average(num1, num2):
    total = num1 + num2
    return(total/2)
num3 = average(7,9)
print(num3)

#Variables defined in a function dont work outside of the function
def list_benefits():
    a = 'More organized code'
    b = "More readable code"
    c = "Easier code reuse"
    d = "Allowing programmers to share and connect code together"
    return a, b, c, d
print(list_benefits())
