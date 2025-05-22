import psycopg2


# Функция подключения к БД
def get_connection():
    return psycopg2.connect(
        dbname="farming_db",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )


# Создание таблиц
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS districts (
            district_id SERIAL PRIMARY KEY,
            district_name TEXT NOT NULL,
            region_name TEXT NOT NULL,
            head_name TEXT
        );

        CREATE TABLE IF NOT EXISTS crops (
            crop_id SERIAL PRIMARY KEY,
            crop_name TEXT NOT NULL,
            crop_family TEXT
        );

        CREATE TABLE IF NOT EXISTS yields (
            district_id INT NOT NULL,
            crop_id INT NOT NULL,
            year INT NOT NULL,
            yield NUMERIC,
            PRIMARY KEY (district_id, crop_id, year),
            FOREIGN KEY (district_id) REFERENCES districts(district_id),
            FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Таблицы созданы")


# Функция добавления района
def insert_district():
    district_name = input("Введите название района: ")
    region_name = input("Введите название области: ")
    head_name = input("Введите главу администрации: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO districts (district_name, region_name, head_name) 
        VALUES (%s, %s, %s)
    """, (district_name, region_name, head_name))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Район добавлен")


# Функция вывода всех районов
def get_all_districts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM districts")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    for row in rows:
        print(row)


# Функция удаления района по названию
def delete_district():
    district_name = input("Введите название района для удаления: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM districts WHERE district_name = %s", (district_name,))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Район {district_name} удалён")


# Главное меню программы
def main():
    while True:
        print("\n=== Меню ===")
        print("1. Создать таблицы")
        print("2. Добавить район")
        print("3. Показать все районы")
        print("4. Удалить район")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            create_tables()
        elif choice == "2":
            insert_district()
        elif choice == "3":
            get_all_districts()
        elif choice == "4":
            delete_district()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("⚠ Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
