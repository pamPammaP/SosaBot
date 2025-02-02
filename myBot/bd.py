import sqlite3


def db_create():
    """Создает базу данных из времени сосания и id чата"""
    
    query = '''CREATE TABLE IF NOT EXISTS database_main (
        "id_chat" INTEGER,
        "time" TEXT);'''

    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS database_main")
    con.execute(query)
    con.close()
    return 1

def write_chat(new_time, chat_id):
    """Записывает значение времени сосания для нового id чата"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("""INSERT OR REPLACE INTO database_main (id_chat, time) VALUES (?, ?)""", (chat_id, new_time))
    con.commit()

def write_time(new_time, chat_id):
    """Записывает новое значение времени сосания по id чата"""
    con = sqlite3.Connection('db_main.db')
    con.execute("UPDATE database_main SET time = ? WHERE id_chat = ?", (new_time, chat_id))
    con.commit()
    con.close()
    return 1

def get_time(chat_id):
    """Возвращает значение времени сосания по id чата"""
    con = sqlite3.Connection('db_main.db')
    cursor = con.cursor()
    cursor.execute("SELECT time FROM database_main WHERE id_chat = ?", (chat_id,))
    result = cursor.fetchone()
    con.close()
    return result