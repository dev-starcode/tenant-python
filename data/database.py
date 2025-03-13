DATABASE_CONFIG = {
    "dbname": "multitenant",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432",
}
import psycopg2
from flask import g

class DatabaseRepository:
    def __init__(self):
        self.connection = psycopg2.connect(**DATABASE_CONFIG)

        # Ajusta o search_path para o schema do middleware
        if hasattr(g, "set_schema") and callable(g.set_schema):
            g.set_schema(self.connection)

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()

    def fetch_all(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
