import sqlite3
from typing import List, Any

def connect_to_db(conn_str: str) -> sqlite3.Connection:
    conn = sqlite3.connect(conn_str)
    return conn

def execute_query(conn: sqlite3.Connection, query: str) -> List[tuple]:
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def insert_record(conn: sqlite3.Connection, table: str, data: dict) -> None:
    cols = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    conn.execute(sql, tuple(data.values()))
    conn.commit()

def close_connection(conn: sqlite3.Connection) -> None:
    conn.close()

class DatabaseManager:
    def __init__(self, conn_str: str):
        self.conn = connect_to_db(conn_str)

    def fetch_all(self, table: str) -> List[tuple]:
        return execute_query(self.conn, f"SELECT * FROM {table}")

    def add(self, table: str, data: dict) -> None:
        insert_record(self.conn, table, data)

    def shutdown(self) -> None:
        close_connection(self.conn)