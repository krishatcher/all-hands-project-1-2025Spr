"""This module provides functions to compare a value against elements in a container
(list, set, or dict) and benchmark the time taken for these comparisons."""

import time


# Function to perform equality comparisons between a passed value and values in the container
def compare_value_in_container(value: any, container: (list | set | dict)) -> list:
    """
    Compare the passed value with each element in the container.
    """
    # Depending on the type of container, loop through and compare values
    if isinstance(container, (list, set)):
        # For lists and sets, compare directly to each element
        return [value == item for item in container]

    elif isinstance(container, dict):
        # For dictionaries, compare the value against each key-value pair
        return [value == container[key] for key in container]

    else:
        raise TypeError("Unsupported container type")


# Function to benchmark the time taken for comparisons in containers
def benchmark_comparison(value: any, container: (list | set | dict)) -> float:
    """
    Benchmark the time it takes to perform equality comparisons on the container.
    """
    start_time = time.perf_counter()  # Start the timer

    # Perform the comparison using the compare_value_in_container function
    compare_value_in_container(value, container)

    end_time = time.perf_counter()  # End the timer
    return end_time - start_time  # Return the duration taken for comparison
