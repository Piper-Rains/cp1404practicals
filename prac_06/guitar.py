
CURRENT_YEAR = 2020
VINTAGE_AGE = 50


class Guitar:
    """A class that allows you to store Guitars with their attributes"""

    def __init__(self, name="", year=0, cost=0):
        """Create attribute fields for Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string to display Guitar information"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar in years based on current year and year of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is 50 or more years old"""
        return self.get_age() >= VINTAGE_AGE

