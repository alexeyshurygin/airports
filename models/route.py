# models/route.py
import sqlite3

class Route:
    def __init__(self, db_path='airports.db'):
        self.conn = sqlite3.connect(db_path)

    def get_routes_between_cities(self, city1, city2):
        query = """
        SELECT * FROM routes
        WHERE (source_city = ? AND destination_city = ?)
        OR (source_city = ? AND destination_city = ?)
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (city1, city2, city2, city1))
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()
