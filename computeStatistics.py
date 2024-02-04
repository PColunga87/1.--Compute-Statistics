# pylint: disable=C0103
"""
P1 - Codigo utilizado para realizar algunas estadisticas
"""
import time
import sys
import math

def calculate_mean(data):
    """
    Compute the mean of a list of numbers.
    """
    return sum(data) / len(data) if len(data) > 0 else 0

def calculate_median(data):
    """
    Compute the median of a list of numbers.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    return sorted_data[n // 2]

def calculate_mode(data):
    """
    Compute the mode of a list of numbers.
    """
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    return modes[0] if modes else None  # Return the first mode if exists

def calculate_standard_deviation(data, mean):
    """
    Compute the standard deviation of a list of numbers.
    """
    variance = sum((x - mean) ** 2 for x in data) / len(data) if len(data) > 0 else 0
    return math.sqrt(variance)

def calculate_variance(data, mean):
    """
    Compute the variance of a list of numbers.
    """
    return sum((x - mean) ** 2 for x in data) / len(data) if len(data) > 0 else 0

def handle_invalid_data(data_str):
    """
    Handle invalid data by attempting to convert it to a float.
    If conversion fails, remove non-numeric characters and count the data.
    """
    try:
        return float(data_str)
    except ValueError:
        numeric_value = ''.join(char for char in data_str if char.isdigit() or char == '.')
        if numeric_value:
            print(f"Converted non-numeric data: {data_str} to {numeric_value}")
            return float(numeric_value)
        print(f"Ignoring invalid data: {data_str}")
        return None

def read_data_from_file(filename):
    """
    Read data from a file and handle invalid entries.
    """
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for item in line.split():
                valid_data = handle_invalid_data(item)
                if valid_data is not None:
                    data.append(valid_data)
    return data

def process_file(filename):
    """
    Process a single file and return statistics.
    """
    start_time = time.time()

    data = read_data_from_file(filename)

    count = len(data)
    mean_value = calculate_mean(data)
    median_value = calculate_median(data)
    mode_value = calculate_mode(data)
    std_deviation_value = calculate_standard_deviation(data, mean_value)
    variance_value = calculate_variance(data, mean_value)

    end_time = time.time()
    elapsed_time = end_time - start_time

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return (
        count, mean_value, median_value, mode_value,
        std_deviation_value, variance_value, elapsed_time, timestamp
    )

def main():
    """
    Main function to compute and display statistics for multiple files.
    """
    if len(sys.argv) != 1:
        print("Usage: python compute_statistics.py")
        sys.exit(1)

    # Prepare data for StatisticsResults.txt
    headers = ["TC", "COUNT", "MEAN", "MEDIAN", "MODE", "SD", "VAR", "Elapsed Time", "Timestamp"]
    file_results = []

    # Process files TC1 to TC7
    for i in range(1, 8):
        filename = f"TC{i}.txt"
        result = [f"TC{i}"] + list(map(str, process_file(filename)))
        file_results.append(result)

    # Display the table
    max_lengths = [max(len(str(row[i])) for row in file_results) for i in range(len(headers))]

    # Print headers
    print('\t'.join(f"{header:<{max_length}}" for header, max_length in zip(headers, max_lengths)))

    # Print data
    for row in file_results:
        print('\t'.join(f"{value:<{max_length}}" for value, max_length in zip(row, max_lengths)))

    # Save the table to a file
    with open("StatisticsResults.txt", 'w', encoding='utf-8') as result_file:
        # Write headers
        result_file.write('\t'.join(headers) + '\n')
        # Write data
        for row in file_results:
            result_file.write('\t'.join(map(str, row)) + '\n')

if __name__ == "__main__":
    main()
