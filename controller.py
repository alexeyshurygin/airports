# controller.py
from models.airport import Airport
from models.route import Route

class Controller:
    def __init__(self):
        self.airport_model = Airport()
        self.route_model = Route()

    def filter_airports(self, min_lat, max_lat, min_lon, max_lon):
        return self.airport_model.filter_by_lat_lon(min_lat, max_lat, min_lon, max_lon)

    def get_routes(self, city1, city2):
        return self.route_model.get_routes_between_cities(city1, city2)
