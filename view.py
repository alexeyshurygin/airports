# view.py
import tkinter as tk
from tkinter import ttk
from controller import Controller

class AirportApp:
    def __init__(self, root):
        self.controller = Controller()
        self.root = root
        self.root.title("Airport Data")

        # Latitude and Longitude input fields
        self.min_lat_label = tk.Label(root, text="Min Latitude")
        self.min_lat_label.grid(row=0, column=0)
        self.min_lat_entry = tk.Entry(root)
        self.min_lat_entry.grid(row=0, column=1)

        self.max_lat_label = tk.Label(root, text="Max Latitude")
        self.max_lat_label.grid(row=1, column=0)
        self.max_lat_entry = tk.Entry(root)
        self.max_lat_entry.grid(row=1, column=1)

        self.min_lon_label = tk.Label(root, text="Min Longitude")
        self.min_lon_label.grid(row=2, column=0)
        self.min_lon_entry = tk.Entry(root)
        self.min_lon_entry.grid(row=2, column=1)

        self.max_lon_label = tk.Label(root, text="Max Longitude")
        self.max_lon_label.grid(row=3, column=0)
        self.max_lon_entry = tk.Entry(root)
        self.max_lon_entry.grid(row=3, column=1)

        # Filter button
        self.filter_button = tk.Button(root, text="Apply Filter", command=self.apply_filter)
        self.filter_button.grid(row=4, column=0, columnspan=2)

        # Table for displaying airports
        self.tree = ttk.Treeview(root, columns=("City", "Country", "Latitude", "Longitude"), show='headings')
        self.tree.heading("City", text="City")
        self.tree.heading("Country", text="Country")
        self.tree.heading("Latitude", text="Latitude")
        self.tree.heading("Longitude", text="Longitude")
        self.tree.grid(row=5, column=0, columnspan=2)

    def apply_filter(self):
        min_lat = float(self.min_lat_entry.get())
        max_lat = float(self.max_lat_entry.get())
        min_lon = float(self.min_lon_entry.get())
        max_lon = float(self.max_lon_entry.get())

        airports = self.controller.filter_airports(min_lat, max_lat, min_lon, max_lon)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for airport in airports:
            self.tree.insert("", "end", values=airport)

if __name__ == "__main__":
    root = tk.Tk()
    app = AirportApp(root)
    root.mainloop()
