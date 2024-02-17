# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class Hotel"""

import json
import unittest
from Work.hotel.hotel import Hotel
from Work.customer.customer import Customer


class TestHotel(unittest.TestCase):
    """
    Test cases for the Hotel class.
    """

    def setUp(self):
        with open("Json/hotel.json", encoding="utf-8") as file:
            self.hotel_data = json.load(file)
            print("Hotel Data:", self.hotel_data)

    def test_create_hotel(self):
        """
        Test creating a Hotel instance.
        """
        for data in self.hotel_data:
            hotel = Hotel(data["name"], data["location"], data["rooms"])
            self.assertEqual(hotel.name, data["name"])
            self.assertEqual(hotel.location, data["location"])
            self.assertEqual(hotel.rooms[0].number, data["rooms"][0])

    def test_reserve_cancel_room(self):
        """
        Test reserving and canceling a room in the hotel.
        """
        for data in self.hotel_data:
            hotel = Hotel(data["name"], data["location"], data["rooms"])
            customer = Customer("John Doe", "john@example.com")
            reservation = hotel.reserve_room(customer, data["rooms"][0])
            self.assertEqual(len(hotel.reservations), 1)
            hotel.cancel_reservation(reservation)
            self.assertEqual(len(hotel.reservations), 0)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
