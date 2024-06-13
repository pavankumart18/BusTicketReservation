# Bus Reservation System

This is a simple bus reservation system that allows users to reserve seats on a bus. The system ensures that seat allocation respects gender-based adjacency preferences and provides a visual representation of the seating arrangement.

## Project Structure

The project consists of the following main components:

1. **Bus Class**: Represents a bus with its details.
2. **Person Class**: Represents a person with their details.
3. **Box Class**: Represents the seating arrangement in the bus.
4. **Reservation Class**: Handles the reservation process.
5. **Berth Allotment Function**: Allocates a berth based on availability and gender.

## Class and Function Descriptions

### Bus Class

The `Bus` class initializes a bus object with its number, starting point, ending point, and timings. It also includes a method to return a string representation of the bus details.

### Person Class

The `Person` class initializes a person object with their name, age, and gender. It includes a method to return a string representation of the person's details.

### Box Class

The `Box` class represents the seating arrangement in the bus. It initializes with width, height, and number of seats. It includes a method to draw the seating arrangement, showing reserved and available seats.

### Berth Allotment Function

The berth allotment function allocates a berth based on availability and gender. It ensures that adjacent seats are allocated according to gender preferences.

### Reservation Class

The `Reservation` class handles the reservation process. It collects user details, allocates a berth using the berth allotment function, updates the seating arrangement, and prints the reservation details.

## Running the Project

1. **Ensure all necessary classes and functions are defined in their respective files**:
    - `Bus.py` for the `Bus` class
    - `Person.py` for the `Person` class
    - `Grid.py` for the `Box` class
    - `berth_allotment.py` for the berth allotment function
    - The `Reservation` class and the main function can be in `main.py` or another appropriate file.

2. **Run the main script**:
    ```bash
    python Reservation.py
    ```

3. **Follow the prompts** to reserve seats.

## Features

- **User Input**: Collects user details such as name, age, and gender.
- **Berth Allotment**: Allocates seats based on availability and gender-based adjacency preferences.
- **Visual Representation**: Provides a visual representation of the seating arrangement.
- **Reservation Details**: Displays the reservation details after each successful booking.

## Future Enhancements

- **Error Handling**: Improve input validation and error handling.
- **Database Integration**: Store reservations in a database for persistence.
- **Web Interface**: Create a web interface for easier access and usability.
