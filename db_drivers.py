import sqlite3
import html


def find_next_id(table_name):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    sanitize(table_name)
    query = f'SELECT COUNT(id) FROM {table_name}'
    cur.execute(query)
    result = cur.fetchone()
    
    con.close()  # Close the connection

    return result[0] + 1


def sanitize(query):
    return html.escape(query)


def get_cursor():
    con = sqlite3.connect("tutorial.db")
    return con.cursor()


def get_cursor_and_connection():
    con = sqlite3.connect("tutorial.db")
    return con.cursor(), con
