# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class reservation"""

import json
import unittest
from Work.reservation.reservation import Reservation
from Work.customer.customer import Customer
from Work.hotel.hotel import Hotel
from Work.room.room import Room


class TestReservation(unittest.TestCase):
    """
    Test cases for the Reservation class.
    """

    def setUp(self):
        with open("Json/reservation.json", encoding="utf-8") as file:
            self.reservation_data = json.load(file)
            print("Reservation Data:", self.reservation_data)

    def test_create_reservation(self):
        """
        Test creating a Reservation instance.
        """
        customer = Customer("John Doe", "john@example.com")
        hotel = Hotel("Sample Hotel", "City Center", [101, 102, 103])
        room = Room(101)
        reservation = Reservation(customer, hotel, room)
        self.assertEqual(reservation.customer, customer)
        self.assertEqual(reservation.hotel, hotel)
        self.assertEqual(reservation.room, room)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
