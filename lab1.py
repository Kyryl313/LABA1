class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #__приватна змінна

    def get_age(self): #метод для отримання значення приватної змінної
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def introduce(self):
        print(f"Мене звати {self.name}, мені {self.__age} років.") #форматуванням рядка в стрінг(f)

    def work(self):
        print("Людина працює.")


class Student(Human): #дочірній клас від хюман
    def __init__(self, name, age, university):
        super().__init__(name, age) #для виклику методів хюман, щоб викликати ініт та створити(ініціалізувати) в студент age і name, замість дублювання
        self.university = university #атрибут тільки для студентів

    def work(self): #поліморфізм/перевизначення
        print("Студент навчається.")

    def study(self):
        print(f"{self.name} навчається в {self.university}.")