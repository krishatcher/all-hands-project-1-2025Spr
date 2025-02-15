"""Test suite for random strings module"""

from typing import Dict, List, Set

from comparison import random_strings

FIVE = 5
TWENTY = 20
HUNDRED = 100


def test_generate_random_string_1():
    """Confirm that output is correct length"""
    result = random_strings.generate_random_string(TWENTY)
    assert isinstance(result, str)
    assert len(result) == TWENTY


def test_generate_random_string_2():
    """Confirm that output is correct length"""
    result = random_strings.generate_random_string(HUNDRED)
    assert isinstance(result, str)
    assert len(result) == HUNDRED


def test_generate_list_of_random_strings():
    """Confirm output of list of random strings"""
    result = random_strings.generate_list_of_random_strings(FIVE, TWENTY)
    assert isinstance(result, List)
    assert len(result) == FIVE
    assert len(result[1]) == TWENTY


def test_generate_set_of_random_strings():
    """Confirm output of set of random strings"""
    result = random_strings.generate_set_of_random_strings(FIVE, TWENTY)
    assert isinstance(result, Set)
    assert len(result) == FIVE
    assert len(result.pop()) == TWENTY


def test_generate_dict_of_random_strings():
    """Confirm output of set of random strings"""
    result = random_strings.generate_dict_of_random_strings(FIVE, TWENTY)
    assert isinstance(result, Dict)
    assert len(result) == FIVE
    assert len(result[1]) == TWENTY
