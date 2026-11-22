print("__"*20)
g = (x for x in [1, 2, 3, 4, 5, 6] if x > 1)
print(list(g))

print("--"*20)

def announce(func):
    def wrapper():
        print("Начинаем")
        result = func()
        print("Готово")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")
hello()
print("__"*20)