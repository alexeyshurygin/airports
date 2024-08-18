# models/airport.py
import sqlite3

class Airport:
    def __init__(self, db_path='airports.db'):
        self.conn = sqlite3.connect(db_path)

    def filter_by_lat_lon(self, min_lat, max_lat, min_lon, max_lon):
        query = """
        SELECT city, country, latitude, longitude FROM airports
        WHERE latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (min_lat, max_lat, min_lon, max_lon))
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()
