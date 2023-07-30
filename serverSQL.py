import mysql.connector

host = "127.0.0.1"
user = "root"
password = "Turok921326"

# Подключение к серверу MySQL
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    if connection.is_connected():
        print("Подключение успешно установлено!")
    else:
        print("Не удалось подключиться.")
except mysql.connector.Error as e:
    print("Ошибка при подключении к базе данных:", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Подключение закрыто.")

