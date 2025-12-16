class City:
    def __init__(self, name, confirmed, recovered, deaths, active, prev_confirmed=None):
        self.name = name
        self.confirmed = confirmed
        self.recovered = recovered
        self.deaths = deaths
        self.active = active
        self.prev_confirmed = prev_confirmed  # previous day cases (growth ke liye)

    def recovery_rate(self):
        if self.confirmed == 0:
            return 0
        rate = (self.recovered / self.confirmed) * 100
        return rate

    def mortality_rate(self):
        if self.confirmed == 0:
            return 0
        rate = (self.deaths / self.confirmed) * 100
        return rate

    def growth_rate(self):
        if self.prev_confirmed in (None, 0):
            return 0
        return ((self.confirmed - self.prev_confirmed) / self.prev_confirmed) * 100

    # severity colour (for trend / severity indication)
    def severity_level(self):
        if self.active > 20000:
            return "High"
        elif self.active > 10000:
            return "Medium"
        return "Low"

    def __str__(self):
        return f"{self.name}: Confirmed={self.confirmed}, Active={self.active}"
