class Person:
    def __init__(self, name, age, gender):
        """
        Initialize a Person object with name, age, and gender.

        Parameters:
        name (str): The name of the person.
        age (int or str): The age of the person.
        gender (str): The gender of the person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """
        Return a string representation of the person's details.
        """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Example usage:
# person = Person("John Doe", 25, "Male")
# print(person)
