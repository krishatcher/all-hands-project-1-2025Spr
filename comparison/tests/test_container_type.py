"""Tests for the container type module."""

from comparison.container_type import ContainerType

LIST_VAL = "list"
LIST_NAME = "LIST"
SET_VAL = "set"
SET_NAME = "SET"
DICT_VAL = "dict"
DICT_NAME = "DICT"


def test_containment_check_approach_list_name():
    """Confirm that the enum name for `List` is correct."""
    assert ContainerType.LIST.name == LIST_NAME


def test_containment_check_approach_list_val():
    """Confirm that the enum value for `List` is correct."""
    assert ContainerType.LIST.value == LIST_VAL


def test_containment_check_approach_list_string():
    """Confirm that the `str` method returns expected for `List`."""
    assert str(ContainerType.LIST) == LIST_VAL


def test_containment_check_approach_set_name():
    """Confirm that the enum name for `Set` is correct."""
    assert ContainerType.SET.name == SET_NAME


def test_containment_check_approach_set_val():
    """Confirm that the enum value for `Set` is correct."""
    assert ContainerType.SET.value == SET_VAL


def test_containment_check_approach_set_string():
    """Confirm that the `str` method returns expected for `Set`."""
    assert str(ContainerType.SET) == SET_VAL


def test_containment_check_approach_dict_name():
    """Confirm that the enum name for `Dict` is correct."""
    assert ContainerType.DICT.name == DICT_NAME


def test_containment_check_approach_dict_val():
    """Confirm that the enum value for `Dict` is correct."""
    assert ContainerType.DICT.value == DICT_VAL


def test_containment_check_approach_dict_string():
    """Confirm that the `str` method returns expected for `Dict`."""
    assert str(ContainerType.DICT) == DICT_VAL
