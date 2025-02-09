from test_suite import generate_random_strings, measure_lookup_time
import pytest

@pytest.fixture
def test_data():
    """Generate data for different containers"""
    test_strings = generate_random_strings(10000)
    return {
        "set": set(test_strings),
        "dict": {s: None for s in test_strings},
        "list": test_strings,
        "test_strings": test_strings
    }

def test_set_lookup(test_data):
    """Test Lookup time for a Set container"""
    time_taken = measure_lookup_time(test_data["set"], test_data["test_strings"])
    return time_taken

def test_dict_lookup(test_data):
    """Test lookup time for a Dict container."""
    time_taken = measure_lookup_time(test_data["dict"], test_data["test_strings"])
    assert time_taken < 0.05, "Dict lookup should be very fast"

def test_list_lookup(test_data):
    """Test lookup time for a List container."""
    time_taken = measure_lookup_time(test_data["list"], test_data["test_strings"])
    assert time_taken > 0.1, "List lookup should be significantly slower"