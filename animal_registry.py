from animal import Animal, Pet, PackAnimal
import mysql.connector



class AnimalRegistry:
    def __init__(self, db_config):
        self.db_config = db_config
        self.animals = []
        self.connection = None

    def connect_to_database(self):
        self.connection = mysql.connector.connect(**self.db_config)
        self.connection.autocommit = True

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def add_animal(self, animal):
        pass

    def classify_animal(self, animal):
    
        pass

    def list_commands(self, name):
        pass

    def train_animal(self, name, new_command):
        pass

    def main_menu(self):
 
        pass

    def run(self):
        self.connect_to_database()
        while True:
            choice = self.main_menu()

        self.close_connection()


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def classify_animal(self, animal):
        if isinstance(animal, Pet):
            return "Домашние животные"
        elif isinstance(animal, PackAnimal):
            return "Вьючные животные"
        else:
            return "Неизвестный тип животного"

    def list_commands(self, name):
        found_animal = None
        for animal in self.animals:
            if animal.name == name:
                found_animal = animal
                break

        if found_animal:
            commands = found_animal.get_commands()
            print(f"{found_animal.name} выполняет следующие команды: {', '.join(commands)}")
        else:
            print("Животное с таким именем не найдено в реестре.")

    def train_animal(self, name, new_command):
        found_animal = None
        for animal in self.animals:
            if animal.name == name:
                found_animal = animal
                break

        if found_animal:
            found_animal.add_command(new_command)
            print(f"Животное {name} успешно обучено новой команде.")
        else:
            print("Животное с таким именем не найдено.")

    def main_menu(self):
        print("\n== Реестр домашних животных ==")
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выйти из программы")
        choice = input("Выберите опцию (1/2/3/4/5): ")
        return choice

    def run(self):
        while True:
            choice = self.main_menu()

            if choice == "1":
                name = input("Введите имя животного: ")
                animal_type = input("Это домашнее (pet) или вьючное животное(pack)?: ")

                if animal_type.lower() == "pet":
                    animal = Pet(name)
                elif animal_type.lower() == "pack":
                    animal = PackAnimal(name)
                else:
                    print("Некорректный тип животного. Попробуйте еще раз.")
                    continue

                with Счетчик():
                    self.add_animal(animal)
                    print(f"{animal_type.capitalize()} животное {name} успешно добавлено в реестр.")

            elif choice == "2":
                name = input("Введите имя животного: ")

                found_animal = None
                for animal in self.animals:
                    if animal.name == name:
                        found_animal = animal
                        break

                if found_animal:
                    animal_class = self.classify_animal(found_animal)
                    print(f"{found_animal.name} относится к классу: {animal_class}")
                else:
                    print("Животное с таким именем не найдено")

            elif choice == "3":
                name = input("Введите имя животного: ")
                self.list_commands(name)

            elif choice == "4":
                name = input("Введите имя животного: ")
                new_command = input("Введите новую команду для животного: ")
                self.train_animal(name, new_command)

            elif choice == "5":
                print("Выход из программы.")
                break

            else:
                print("Некорректный выбор. Попробуйте еще раз.")


class Счетчик:
    def __init__(self):
        self.value = 0
        self.opened = False

    def add(self):
        if not self.opened:
            raise Exception("Работа с объектом типа 'Счетчик' должна быть в блоке try-with-resources.")
        self.value += 1

    def __enter__(self):
        self.opened = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.opened = False
        if exc_type is not None:
            print("Произошло исключение:", exc_value)

if __name__ == "__main__":
    db_config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "Turok921326"
    }

    registry = AnimalRegistry(db_config)
    registry.run()

