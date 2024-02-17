# pylint: disable=C0103
# pylint: disable=W0718

"""Code to execute the class Customer"""
import unittest
import json
from Work.customer.customer import Customer


class TestCustomer(unittest.TestCase):
    """
    Test cases for the Customer class.
    """

    def setUp(self):
        with open("Json/customer.json", encoding="utf-8") as file:
            self.customer_data = json.load(file)
            print("Customer Data:", self.customer_data)

    def test_create_customer(self):
        """
        Test creating a Customer instance.
        """
        for data in self.customer_data:
            customer = Customer(data["name"], data["email"])
            self.assertEqual(customer.name, data["name"])
            self.assertEqual(customer.email, data["email"])

    def test_modify_customer_information(self):
        """
        Test modifying customer information.
        """
        for data in self.customer_data:
            customer = Customer(data["name"], data["email"])
            customer.modify_information("Jane Doe", "jane@example.com")
            self.assertEqual(customer.name, "Jane Doe")
            self.assertEqual(customer.email, "jane@example.com")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
