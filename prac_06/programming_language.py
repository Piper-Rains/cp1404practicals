
class ProgrammingLanguage:
    """A simple class to compare different programing languages"""

    def __int__(self, name, typing, reflection, year):
        """Create fields for given programming language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string to display ProgrammingLanguage information"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)
