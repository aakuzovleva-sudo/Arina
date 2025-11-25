import pandas as pd


def write_to_excel():
    """Функция для записи данных пользователя в Excel файл"""

    print("=== Запись данных в Excel файл ===")

    # Получаем данные от пользователя
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    email = input("Введите ваш email: ")
    city = input("Введите ваш город: ")

    # Создаем словарь с данными
    data = {
        'Имя': [name],
        'Возраст': [age],
        'Email': [email],
        'Город': [city]
    }

    # Создаем DataFrame
    df = pd.DataFrame(data)

    # Записываем в Excel файл
    filename = 'user_data.xlsx'
    df.to_excel(filename, index=False)

    print(f"\nДанные успешно записаны в файл: {filename}")
    print("Содержимое файла:")
    print(df)


# Дополнительная функция для записи нескольких записей
def write_multiple_records():
    """Функция для записи нескольких записей в Excel"""

    print("\n=== Запись нескольких записей ===")
    records = []

    while True:
        print(f"\nЗапись #{len(records) + 1}")
        name = input("Введите имя (или 'стоп' для завершения): ")

        if name.lower() == 'стоп':
            break

        age = input("Введите возраст: ")
        email = input("Введите email: ")
        city = input("Введите город: ")

        records.append({
            'Имя': name,
            'Возраст': age,
            'Email': email,
            'Город': city
        })

    if records:
        df = pd.DataFrame(records)
        filename = 'multiple_users_data.xlsx'
        df.to_excel(filename, index=False)
        print(f"\nЗаписано {len(records)} записей в файл: {filename}")
        print(df)
    else:
        print("Не было введено ни одной записи")


if __name__ == "__main__":
    # Основная программа
    while True:
        print("\nВыберите действие:")
        print("1 - Записать одну запись")
        print("2 - Записать несколько записей")
        print("3 - Выйти")

        choice = input("Ваш выбор (1/2/3): ")

        if choice == '1':
            write_to_excel()
        elif choice == '2':
            write_multiple_records()
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова")