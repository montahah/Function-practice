#Function
def test():
    print("Hello Stranger")

test()

#Function with parameters
def test2(x, y):
    print("Addition x+y: ", x+y)

test2(1,3)

# Function for validation
def is_valid_age():
    age = int(input("Age: "))
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"



numbers = [1, 2, 3, 4, 5]
def square(x):
    return x*x
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)
# print(square)

def greet(name):
    print(f"Hello, {name}")
greet("Montaha")

def info(name, age = 18):
    print(f"{name} is {age} years old")
info("Karim")
info("Masud", 25)
info("Khalil", 42)

def add_numbers(*nums):
    return sum(nums * 3)
print(add_numbers(2, 3, 4))

def print_details(**details):
    for key, value in details.items():
        print(f"{key} : {value}")
print_details(name="Montaha", age= 30, country= "Bangladesh")

def add(a,b):
    return a+b
print(add(2,3))

def create_list():
    return [1,2,3]
print(create_list())

def stats(a,b):
    return a+b, a-b
print(stats(10, 5))

x = 100
def test():
    y = 50
    print(y)
    print(x)
test()
print(x)



