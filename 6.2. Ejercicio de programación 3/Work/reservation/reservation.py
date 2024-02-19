# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""


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
