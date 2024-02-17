# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""

import json


class Room:
    """
    Represents a room.

    Attributes:
    - number (int): The room number.
    """

    def __init__(self, number):
        """
        Initialize a Room instance.

        Parameters:
        - number (int): The room number.
        """
        self.number = number

    @classmethod
    def load_from_json(cls, file_path):
        """
        Load room data from a JSON file.

        Parameters:
        - file_path (str): The path to the JSON file.

        Returns:
        list: List of Room instances.
        """
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        rooms = [cls(room_data['number']) for room_data in data]
        return rooms
