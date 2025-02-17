"""Perform an experiment to determine performance of string comparisons using different container types"""

import timeit
from typing import Dict, List, Set, Union

import typer
from rich.console import Console

from comparison import comparison_logic, random_strings
from comparison.container_type import ContainerType

# Define the CLI
cli = typer.Typer()
console = Console()


# Generate random container and value
def generate_random_container(
    size: int, maximum: int, container_type: ContainerType
) -> Union[list, dict, set]:
    """Generate the random container, calling the `random_strings` file"""
    if container_type == ContainerType.LIST:
        return random_strings.generate_list_of_random_strings(size, maximum)
    elif container_type == ContainerType.DICT:
        return random_strings.generate_dict_of_random_strings(size, maximum)
    elif container_type == ContainerType.SET:
        return random_strings.generate_set_of_random_strings(size, maximum)
    else:
        empty_result: List[str] = []
        return empty_result


# Perform the containment check benchmark
def perform_containment_check_benchmark(
    value: str,
    # The value to compare against elements in the container.
    container: (list | set | dict),
    # The container holding the elements to compare against.
    number_runs: int = 10,
    # The number of runs per benchmark.
    number_repeats: int = 3,
    # The number of times to repeat the benchmark.
) -> List[float]:
    """
    Run an experiment using the timeit package for the specific function.

    This function benchmarks the comparison of a value against elements in a container
    using the `benchmark_comparison` function. It runs the comparison `number_runs` times
    per benchmark and repeats the benchmark `number_repeats` times to get a reliable measurement.

    Args:
        value (str): The value to compare against elements in the container.
        container (list | set | dict): The container holding the elements to compare against.
        number_runs (int): The number of runs per benchmark.
        number_repeats (int): The number of times to repeat the benchmark.
    """
    times = timeit.repeat(
        # Perform the benchmark using the `benchmark_comparison` function
        lambda: comparison_logic.compare_value_in_container(value, container),
        number=number_runs,
        repeat=number_repeats,
    )

    return times


def output_results(
    times: List[float],
    number_runs: int,
    number_repeats: int,
    str_length: int,
    container_type: ContainerType,
) -> None:
    """Output experiment results to console"""
    # Get the minimum time taken
    min_time = min(times)
    # Get the maximum time taken
    max_time = max(times)
    # Calculate the average time taken
    avg_time = sum(times) / len(times)

    console.print(" =============================================== ")
    console.print(" =              Benchmark Results              = ")
    console.print(" =============================================== ")
    console.print(f" Number of Benchmarks: {number_repeats}")
    console.print(f" Number of Runs per Benchmark: {number_runs}")
    console.print(f" String Length: {str_length}")
    console.print(f" Container Type: {container_type}")
    console.print(" ----------------------------------------------- ")
    console.print(f" Min execution time: {min_time:.6f} seconds")
    console.print(f" Avg execution time: {avg_time:.6f} seconds")
    console.print(f" Max execution time: {max_time:.6f} seconds")
    console.print(" ----------------------------------------------- ")


# Main function to run the experimental suite
@cli.command()
def comparison(
    size: int = typer.Option(5000),
    maximum: int = typer.Option(100),
    container_type: ContainerType = ContainerType.LIST
) -> None:
    """The main entry point of this program"""
    number_runs = 10
    number_repeats = 3

    random_container = generate_random_container(size, maximum, container_type)
    # Generate a random value
    random_value = random_strings.generate_random_string(maximum)
    # Perform the containment check benchmark
    times = perform_containment_check_benchmark(
        random_value, random_container, number_runs, number_repeats
    )
    # Output results to console
    output_results(times, number_runs, number_repeats, maximum, container_type)
