class Box:
    def __init__(self, width=3, height=3, no=24):
        """
        Initialize the Box object with width, height, and number of seats.

        Parameters:
        width (int): The width of the box.
        height (int): The height of the box.
        no (int): The total number of seats.
        """
        self.width = width
        self.height = height
        self.no = list(range(1, no + 1))
        self.reserved_seats = {}

    def draw_box(self):
        """
        Draw the seating arrangement of the box.
        """
        for e in range(3):
            l = e
            if e == 2:
                print("-------" * 9)  # Print a separator line after every third column

            for i in range(self.height):
                for j in range(self.width * 8):
                    if j != 0 and j % 3 == 0:
                        print("  ", end="")  # Print a space between columns

                    if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                        if i != 0 and i != self.height - 1:
                            print("| ", end="")  # Print vertical edges
                        else:
                            print("- ", end="")  # Print horizontal edges
                    elif j % self.width == 0 or j % self.width == 2:
                        print("| ", end="")  # Print vertical dividers
                    elif i == self.height // 2 and j % self.width == 1:
                        # Print seat numbers or 'R' for reserved seats
                        if self.no[l] not in self.reserved_seats:
                            if l < 9:
                                print(f'{self.no[l]} ', end="")
                                l += 3
                            else:
                                print(f'{self.no[l]}', end="")
                                l += 3
                        else:
                            l += 3
                            print('R ', end="")
                    else:
                        print(' ', end="")  # Print space for empty seats
                print()  # New line after each row
            print()  # New line after each set of rows
#Testing
# b=Box()
# b.draw_box()
