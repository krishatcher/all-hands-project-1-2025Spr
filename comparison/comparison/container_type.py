"""Configuration of the comparison tool with a container type."""

from enum import Enum


class ContainerType(str, Enum):
    """Enum defining available container type names"""

    LIST = "list"
    SET = "set"
    DICT = "dict"

    def __str__(self):
        """Overloaded dunder string method to return the value"""
        return self.value
