print("__"*20)
x = 31

def show():
    x = 21
    print(x)

show()
print(x)

print("--"*20)

def total(*args):
    return sum(args)

print(total(21, 22, 23))

print("--"*20)

def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Вадим", age=17))

print("--"*20)

def increase(x):
    return x + 1

def apply(func, value):
    return func(value)

print(apply(increase, 2))

print("--"*20)

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(2)
print("__"*20)