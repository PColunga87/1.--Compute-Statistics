# pylint: disable=C0103
# pylint: disable=W0718
"""
Script tarea 5.2
"""


import json
import time
import sys


def compute_sales(price_catalogue, *sales_records_list):
    """
    Compute the total cost for sales based on
    a price catalogue for multiple sales records.

    Args:
        price_catalogue (str): Path to the JSON file
        containing price information.
        sales_records_list (list): Paths to the JSON
        files containing sales records.

    Returns:
        None
    """
    try:
        with open(price_catalogue, 'r', encoding='utf-8') as price_file:
            price_data = json.load(price_file)

        with open('SalesResults.txt', 'w', encoding='utf-8') as results_file:
            for sales_record in sales_records_list:
                total_cost = 0
                with open(sales_record, 'r', encoding='utf-8') as sales_file:
                    sales_data = json.load(sales_file)

                    for sale in sales_data:
                        product_name = sale.get('Product')
                        quantity = sale.get('Quantity')
                        if product_name and quantity:
                            matching_products = [
                                prod for prod in price_data if prod.get(
                                            'title') == product_name
                            ]
                            if matching_products:
                                product_price = matching_products[0].get(
                                    'price')
                                total_cost += quantity * product_price
                            else:
                                print(
                                    f"Error: {product_name} not found value")
                        else:
                            print("Error: Invalid item format in sales rec")

                results_file.write(f"{sales_record} sum = ${total_cost:.2f}\n")
                print(f"{sales_record} sum = ${total_cost:.2f}")

            elapsed_time = time.process_time()
            results_file.write(f"Time Elapsed: {elapsed_time} seconds\n")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}", file=sys.stderr)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
    except KeyError as e:
        print(f"Error accessing key: {e}", file=sys.stderr)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: python computeSales.py price_catalogue&sales_records.json")
    else:
        price_catalogue_file = sys.argv[1]
        sales_records = sys.argv[2:]
        compute_sales(price_catalogue_file, *sales_records)
