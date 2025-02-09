"""Helper Function"""

import timeit
import random
import string
from typing import List, Union, Dict, Set

def generate_random_strings(n: int, length: int = 8) -> List[str]:
    """Generate a list of `n` random strings of given `length`."""
    return [''.join(random.choices(string.ascii_letters, k=length)) for _ in range(n)]

def measure_lookup_time(container: Union[Set[str], Dict[str, Any], List[str]], 
                        test_strings: List[str], repeat: int = 5) -> float:
    """Measure the time taken to check membership of `test_strings` in `container` using timeit."""
    stmt = "for s in test_strings: _ = s in container"
    setup = "from __main__ import container, test_strings"
    return timeit.timeit(stmt, setup=setup, number=repeat) / repeat  # Averaged over runs
