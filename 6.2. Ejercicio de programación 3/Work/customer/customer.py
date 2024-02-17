
# pylint: disable=C0103
# pylint: disable=W0718
"""Code to execute the class customer"""
import json


class Customer:
    """
    Represents a customer.

    Attributes:
    - name (str): The name of the customer.
    - email (str): The email address of the customer.
    """

    def __init__(self, name, email):
        """
        Initialize a Customer instance.

        Parameters:
        - name (str): The name of the customer.
        - email (str): The email address of the customer.
        """
        self.name = name
        self.email = email

    def display_info(self):
        """
        Display information about the customer.

        Returns:
        str: Information about the customer.
        """
        return f"Customer: {self.name}, Email: {self.email}"

    def modify_information(self, new_name, new_email):
        """
        Display information about the customer.

        Returns:
        str: Information about the customer.
        """
        self.name = new_name
        self.email = new_email

    @classmethod
    def load_from_json(cls, file_path):
        """
        Load customer data from a JSON file.

        Parameters:
        - file_path (str): The path to the JSON file.

        Returns:
        list: List of Customer instances.
        """
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        customers = [cls(
            customer_data['name'],
            customer_data['email']) for customer_data in data]
        return customers
