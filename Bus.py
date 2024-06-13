class Bus:
    def __init__(self, bus_no, start, end, timings):
        """
        Initialize a Bus object with bus number, start and end points, and timings.

        Parameters:
        bus_no (int): The bus number.
        start (str): The starting point of the bus.
        end (str): The ending point of the bus.
        timings (str): The departure time of the bus.
        """
        self.bus_no = bus_no
        self.start = start
        self.end = end
        self.timings = timings
        self.seats = 24  # Total number of seats in the bus

    def __str__(self):
        """
        Return a string representation of the bus details.
        """
        return (
            f"Bus No : {self.bus_no}\n"
            f"Starting : {self.start}\n"
            f"Ending : {self.end}\n"
            f"Time : {self.timings}"
        )

# Example usage:
# bus = Bus(123, "Mumbai", "Pune", "10:00")
# print(bus)
