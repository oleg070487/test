# Функция для добавления записи в файл
def add_record(filename, record):
    with open(filename, 'a') as file:
        file.write(record + '\n')

# Функция для просмотра всех записей из файла
def view_records(filename):
    with open(filename, 'r') as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

# Основная функция приложения
def main():
    filename = 'notes.txt'

    while True:
        print("\nМеню:")
        print("1. Просмотр записей")
        print("2. Добавить запись")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nЗаписи:")
            view_records(filename)
        elif choice == '2':
            record = input("Введите новую запись: ")
            add_record(filename, record)
            print("Запись добавлена.")
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор.")

# Запуск приложения
if __name__ == "__main__":
    main()