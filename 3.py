students = {}

while True:
    name = input("Ім'я студента (або stop): ")
    if name.lower() == "stop":
        break
    grade = int(input("Оцінка: "))
    students[name] = grade

print("Список студентів:",students)

if students:
    avg = sum(students.values()) / len(students)
    print(f"Середній бал: {avg:}")

    excellent = [n for n, g in students.items() if 10 <= g <= 12]
    good = [n for n, g in students.items() if 7 <= g <= 9]
    weak = [n for n, g in students.items() if 4 <= g <= 6]
    failed = [n for n, g in students.items() if 1 <= g <= 3]

    print(f"Відмінники: {len(excellent)}-{excellent}")
    print(f"Хорошисти: {len(good)}-{good}")
    print(f"Відстаючі: {len(weak)}-{weak}")
    print(f"Не здали: {len(failed)}-{failed}")
