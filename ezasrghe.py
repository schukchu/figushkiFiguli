import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")