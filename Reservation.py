from Bus import Bus
from person import Person
from Grid import Box
from berth_allotment import berth_allotment
import random

seats_booked = {}

class Reservation:
    def __init__(self):
        """
        Initialize a Reservation object, collect user details, and allot a berth.
        """
        self.bus = Bus(123, "Mumbai", "Pune", "10:00")

        # Collecting user details
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        while not age.isdigit():
            age = input("Enter a valid age: ")

        gender = input("Enter your gender (Male or Female): ")

        self.person = Person(name, age, gender)
        self.box = Box()

        # Allocate a berth
        self.berth = berth_allotment(seats_booked, gender)
        if self.berth is None:
            print("No seats available")
            return

        # Update the seats_booked dictionary
        seats_booked[self.berth] = gender
        self.box.reserved_seats = seats_booked

        # Draw the current seating arrangement
        self.box.draw_box()

    def __str__(self):
        """
        Return a string representation of the reservation details.
        """
        return f"{self.bus}\nPerson: {self.person}\nSeat No: {self.berth}"

def main():
    """
    Main function to handle the reservation process.
    """
    while True:
        choice = input("Do you want to reserve another seat? (y/n): ")
        if choice.lower() == "y":
            reservation = Reservation()
            print(reservation)
        else:
            break

if __name__ == "__main__":
    main()
