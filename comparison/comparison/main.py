import timeit
from typing import Union

import typer
from rich.console import Console

from comparison import benchmark_comparison

# Define the CLI
cli = typer.Typer()
console = Console()


# Generate random container and value
def generate_random_container(
    size: int, maximum: int, container_type: str
) -> Union[list, dict, set]:
    import random
    import string

    random_strings = [
        "".join(random.choices(string.ascii_letters, k=10))
        for _ in range(size)
    ]
    if container_type == "list":
        # Return a list of random strings
        return random_strings
    elif container_type == "dict":
        # Return a dictionary with random strings as keys and None as values
        return {s: None for s in random_strings}
    elif container_type == "set":
        return set(random_strings)


def generate_random_value(maximum: int, exceed: bool) -> str:
    import random

    # Generate a random string of letters
    import string

    # If exceed is True, generate a string that exceeds the maximum length
    if exceed:
        return "".join(random.choices(string.ascii_letters, k=maximum + 1))
    else:
        return "".join(random.choices(string.ascii_letters, k=maximum))


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
) -> None:
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
        lambda: benchmark_comparison(value, container),
        number=number_runs,
        repeat=number_repeats,
    )
    min_time = min(times)
    # Get the minimum time taken
    max_time = max(times)
    # Get the maximum time taken
    avg_time = sum(times) / len(times)
    # Calculate the average time taken
    total_runs = number_runs * number_repeats
    # Calculate the total number of runs

    console.print(
        f"Benchmark Results ({number_runs} runs per repeat, {number_repeats} repeats):"
    )
    console.print(f"Total runs: {total_runs}")  # Total number of runs
    console.print(f"Min execution time: {min_time:.6f} seconds")
    console.print(f"Max execution time: {max_time:.6f} seconds")
    console.print(f"Avg execution time: {avg_time:.6f} seconds")
    console.print(f"Number of runs per benchmark: {number_runs}")
    console.print(f"Number of repeats: {number_repeats}")


# Main function to run the experimental suite
@cli.command()
def main(
    size: int = typer.Option(..., help="The size of the container."),
    # The maximum value of the integer values stored in the container.
    maximum: int = typer.Option(
        ...,
        help="The maximum value of the integer values stored in the container.",
    ),
    # The type of container to use (list, dict, set).
    container_type: str = typer.Option(
        ..., help="The type of container to use (list, dict, set)."
    ),
    # Whether or not the searching algorithm should look for a value that exceeds the maximum value.
    exceed: bool = typer.Option(
        # Default value is
        False,
        help="Whether or not the searching algorithm should look for a value that exceeds the maximum value.",
        is_flag=True,
    ),
) -> None:  # The return type of the function is None
    random_container = generate_random_container(size, maximum, container_type)
    # Generate a random value
    random_value = generate_random_value(maximum, exceed)
    # Perform the containment check benchmark

    perform_containment_check_benchmark(random_value, random_container)
    # Perform the containment check benchmark


# Entry point of the script
if __name__ == "__main__":
    cli()
