import sqlite3
import html


def sanitize(query):
    return html.escape(query)


def get_cursor():
    con = sqlite3.connect("tutorial.db")
    return con.cursor()


def get_cursor_and_connection():
    con = sqlite3.connect("tutorial.db")
    return con.cursor(), con
