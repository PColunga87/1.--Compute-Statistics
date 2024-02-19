# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""

from Work.room.room import Room
from Work.reservation.reservation import Reservation


class Hotel:
    """
    Represents a hotel.

    Attributes:
    - name (str): The name of the hotel.
    - location (str): The location of the hotel.
    - rooms (list): List of Room instances in the hotel.
    - reservations (list): List of Reservation instances made in the hotel.
    """

    def __init__(self, name, location, rooms):
        """
        Initialize a Hotel instance.

        Parameters:
        - name (str): The name of the hotel.
        - location (str): The location of the hotel.
        - rooms (list): List of room numbers in the hotel.
        """
        self.name = name
        self.location = location
        self.rooms = [Room(number) for number in rooms]
        self.reservations = []

    def display_info(self):
        """
        Display information about the hotel.

        Returns:
        str: Information about the hotel.
        """
        return f"""Hotel: {self.name}, Location: {self.location},
                    Rooms: {[room.number for room in self.rooms]}"""

    def reserve_room(self, customer, room_number):
        """
        Reserve a room in the hotel for a customer.

        Parameters:
        - customer (Customer): The customer making the reservation.
        - room_number (int): The room number to be reserved.

        Returns:
        Reservation: The reservation object.

        Raises:
        ValueError: If the room number is invalid.
        """
        room = next((r for r in self.rooms if r.number == room_number), None)
        if room:
            reservation = Reservation(customer, self, room)
            self.reservations.append(reservation)
            return reservation
        else:
            raise ValueError("Invalid room number")

    def cancel_reservation(self, reservation):
        """
        Cancel a reservation in the hotel.

        Parameters:
        - reservation (Reservation): The reservation to be canceled.

        Raises:
        ValueError: If the reservation is not found.
        """
        if reservation in self.reservations:
            self.reservations.remove(reservation)
        else:
            raise ValueError("Reservation not found")
