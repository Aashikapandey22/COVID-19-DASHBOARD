import csv
import os
from city_class import City


class DataAnalyzer:
    def __init__(self, filename):
        base_dir = os.path.dirname(__file__)
        self.filename = os.path.join(base_dir, filename)
        self.cities = []

    def load_data(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                prev_conf = int(row['PrevConfirmed']) if 'PrevConfirmed' in row and row['PrevConfirmed'] else None
                city = City(
                    row['City'],
                    int(row['Confirmed']),
                    int(row['Recovered']),
                    int(row['Deaths']),
                    int(row['Active']),
                    prev_conf
                )
                self.cities.append(city)

    def critical_cities(self, threshold=20000):
        return [c.name for c in self.cities if c.active > threshold]

    # summary statistics for Report class / dashboard
    def average_recovery_rate(self):
        if not self.cities:
            return 0
        total = sum(c.recovery_rate() for c in self.cities)
        return total / len(self.cities)

    def average_mortality_rate(self):
        if not self.cities:
            return 0
        total = sum(c.mortality_rate() for c in self.cities)
        return total / len(self.cities)

    def average_growth_rate(self):
        if not self.cities:
            return 0
        total = sum(c.growth_rate() for c in self.cities)
        return total / len(self.cities)
