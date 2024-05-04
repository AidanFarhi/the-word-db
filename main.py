import os
import csv
import sqlite3


def create_db():
    if os.path.exists("bible.db"): os.remove("bible.db")
    return sqlite3.connect("bible.db")

def create_table(cursor):
    create_table_statement = """
        CREATE TABLE bible_record (
            book TEXT,
            chapter INTEGER,
            verse INTEGER,
            content TEXT
        );
    """
    cursor.execute(create_table_statement)

def insert_data(cursor):
    insert_statement = 'INSERT INTO bible_record (book, chapter, verse, content) VALUES (?, ?, ?, ?);'
    with open('data/genesis.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            book, chapter, verse, text = row
            cursor.execute(insert_statement, (book, int(chapter), int(verse), text))

def main():
    conn = create_db()
    cursor = conn.cursor()
    create_table(cursor)
    insert_data(cursor)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
