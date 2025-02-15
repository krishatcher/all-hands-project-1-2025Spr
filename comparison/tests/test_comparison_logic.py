"""Test suite for comparison logic module"""

from typing import Dict, List, Set

from comparison import comparison_logic, random_strings

TWENTY = 20
FIVE = 5


def compare_value_in_container_list_present():
    """validate output for list container with value present"""
    testing_list = random_strings.generate_list_of_random_strings(FIVE, TWENTY)
    testing_value = testing_list[2]

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_list
    )
    assert isinstance(result, List)
    assert len(result) >= 1
    assert result[0] == testing_value


def compare_value_in_container_list_not_present():
    """validate output for list container with value present"""
    testing_list = random_strings.generate_list_of_random_strings(FIVE, TWENTY)
    testing_value = "string is not present"

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_list
    )
    assert isinstance(result, List)
    assert len(result) == 0


def compare_value_in_container_set_present():
    """validate output for set container with value present"""
    testing_set = random_strings.generate_set_of_random_strings(FIVE, TWENTY)
    testing_value = testing_set[2]

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_set
    )
    assert isinstance(result, Set)
    assert len(result) >= 1
    assert result[0] == testing_value


def compare_value_in_container_set_not_present():
    """validate output for set container with value present"""
    testing_set = random_strings.generate_set_of_random_strings(FIVE, TWENTY)
    testing_value = "string is not present"

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_set
    )
    assert isinstance(result, Set)
    assert len(result) == 0


def compare_value_in_container_dict_present():
    """validate output for dict container with value present"""
    testing_dict = random_strings.generate_dict_of_random_strings(FIVE, TWENTY)
    testing_value = testing_dict[2]

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_dict
    )
    assert isinstance(result, Dict)
    assert len(result) >= 1
    assert result[0] == testing_value


def compare_value_in_container_dict_not_present():
    """validate output for dict container with value present"""
    testing_dict = random_strings.generate_dict_of_random_strings(FIVE, TWENTY)
    testing_value = "string is not present"

    result = comparison_logic.compare_value_in_container(
        testing_value, testing_dict
    )
    assert isinstance(result, Dict)
    assert len(result) == 0
