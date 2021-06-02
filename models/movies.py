class Movie:
    def __init__(self, name: str, category: str, rate: float):
        self.name = name
        self.category = category
        self.rate = rate

    def __str__(self):
        return f"{self.name} - {self.rate}"
