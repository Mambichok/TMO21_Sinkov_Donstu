def tasks_per_student(tasks, students):
    if students == 0:
        return ("На ноль делить нельзя")
    else:
        return tasks / students

assert tasks_per_student(10, 2) == 5.0
assert tasks_per_student(10, 0) == "На ноль делить нельзя"
assert tasks_per_student(7, 7) == 1.0
print("__"*20)
print(f"Первая часть: {tasks_per_student(10, 2)}")
print("--"*20)
spisok = ["акт", "задача", "упражнение"]
result = sorted(spisok, key=lambda a: len(a))

print(result)
print("__"*20)
