# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""

import json


class Reservation:
    """
    Represents a reservation.

    Attributes:
    - customer (Customer): The customer making the reservation.
    - hotel (Hotel): The hotel where the reservation is made.
    - room (Room): The room reserved.
    """

    def __init__(self, customer, hotel, room):
        """
        Initialize a Reservation instance.

        Parameters:
        - customer (Customer): The customer making the reservation.
        - hotel (Hotel): The hotel where the reservation is made.
        - room (Room): The room reserved.
        """
        self.customer = customer
        self.hotel = hotel
        self.room = room

    @classmethod
    def load_from_json(cls, file_path, hotels, customers, rooms):
        """
        Load reservation data from a JSON file.

        Parameters:
        - file_path (str): The path to the JSON file.
        - hotels (list): List of Hotel instances.
        - customers (list): List of Customer instances.
        - rooms (list): List of Room instances.

        Returns:
        list: List of Reservation instances.
        """
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        reservations = []
        for reservation_data in data:
            customer = next(
                (c for c in customers
                    if c.name == reservation_data['customer']['name']),
                None)
            hotel = next(
                (h for h in hotels
                    if h.name == reservation_data['hotel']['name']),
                None)
            room_number = reservation_data['room_number']
            room = next(
                (r for r in rooms
                    if r.number == room_number), None)

            if customer and hotel and room:
                reservation = cls(customer, hotel, room)
                reservations.append(reservation)

        return reservations
