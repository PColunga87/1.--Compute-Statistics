# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""

import json
import unittest
from Work.room.room import Room


class TestRoom(unittest.TestCase):
    """
    Test cases for the Room class.
    """

    def setUp(self):
        with open("Json/room.json", encoding="utf-8") as file:
            self.room_data = json.load(file)
            print("Room Data:", self.room_data)

    def test_create_room(self):
        """
        Test creating a Room instance.
        """
        for data in self.room_data:
            room = Room(data["number"])
            self.assertEqual(room.number, data["number"])

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
