# pylint: disable=C0103
"""
Script - Conversion 
"""
import sys
import time

def decimal_to_binary_recursive(n):
    """
    Convert decimal to binary representation using recursion.

    :param n: Decimal number to convert.
    :return: Binary representation as a string.
    """
    if n == 0:
        return '0'
    return (
    '-' + decimal_to_binary_recursive(-n) if n < 0
    else decimal_to_binary_recursive(n // 2) + str(n % 2)
)


def convert_numbers(file_path):
    """
    Convert numbers in a file to binary and hexadecimal bases.

    :param file_path: Path to the file containing a list of numbers.
    :return: Tuple containing lists of binary and hexadecimal results.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            numbers = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

    binary_results = []
    hex_results = []

    for _, number in enumerate(numbers, start=1):
        try:
            num = int(number)
            binary_result = decimal_to_binary_recursive(num)
            hex_result = format(num if num >= 0 else (1 << 32) + num, 'X')
        except ValueError:
            print(f"Error: Invalid data found - '{number}' in the file.")
            binary_result, hex_result = "#VALUE!", "#VALUE!"

        binary_results.append(binary_result)
        hex_results.append(hex_result)

    return binary_results, hex_results, numbers

def write_results_to_file(results_file, binary_results, hex_results, values):
    """
    Write the conversion results to the ConversionResults.txt file.

    :param results_file: File object for writing results.
    :param binary_results: List of binary results.
    :param hex_results: List of hexadecimal results.
    :param values: List of original values from the input file.
    """
    results_file.write("NUMBER\t\tTC\tBIN\tHEX\n")

    for _, (binary, hex_value, value) in enumerate(
        zip(binary_results, hex_results, values), start=1):
        if "Error: Invalid data found" in binary:
            tc_text = value
        else:
            tc_text = f"{value}"

        results_file.write(f"{_}\t{tc_text}\t{binary}\t{hex_value}\n")
        print(f"{_}\t{tc_text}\t{binary}\t{hex_value}")

    results_file.write("\n")

def main():
    """
    Main function to execute the conversion process and display elapsed time.
    """
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py input_file.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]

    start_time = time.time()

    with open("ConversionResults.txt", 'w', encoding='utf-8') as results_file:
        binary_results, hex_results, values = convert_numbers(input_file_path)
        if binary_results is not None:
            write_results_to_file(results_file, binary_results, hex_results, values)

    end_time = time.time()

    print("Conversion results have been written to ConversionResults.txt")

    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

if __name__ == "__main__":
    main()
