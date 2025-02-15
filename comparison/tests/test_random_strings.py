"""Test suite for random strings module"""

from typing import Dict, List, Set
from comparison import random_strings


def test_generate_random_string_1():
    """Confirm that output is correct length"""
    result = random_strings.generate_random_string(20)
    assert isinstance(result, str)
    assert len(result) == 20


def test_generate_random_string_2():
    """Confirm that output is correct length"""
    result = random_strings.generate_random_string(100)
    assert isinstance(result, str)
    assert len(result) == 100


def test_generate_list_of_random_strings():
    """Confirm output of list of random strings"""
    result = random_strings.generate_list_of_random_strings(5, 20)
    assert isinstance(result, List)
    assert len(result) == 5
    assert len(result[1]) == 20


def test_generate_set_of_random_strings():
    """Confirm output of set of random strings"""
    result = random_strings.generate_set_of_random_strings(5, 20)
    assert isinstance(result, Set)
    assert len(result) == 5
    assert len(result.pop()) == 20


def test_generate_dict_of_random_strings():
    """Confirm output of set of random strings"""
    result = random_strings.generate_dict_of_random_strings(5, 20)
    assert isinstance(result, Dict)
    assert len(result) == 5
    assert len(result[1]) == 20
