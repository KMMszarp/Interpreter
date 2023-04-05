from enum import Enum


class Data:
    def __init__(self):
        self.variables = {}

    def create_variable(self, name):
        self.variables[name] = None

    def initialize_variable(self, name, value):
        assert name in self.variables
        self.variables[name] = value

    def create_and_initialize_variable(self, name, value):
        self.create_variable(name)
        self.initialize_variable(name, value)

    def get_variable(self, name):
        return self.variables[name]


class Type(Enum):
    INT = 1
    STRING = 2
    BOOL = 3
    VOID = 4
    ARRAY = 5
    FUNCTION = 6

    ARRAY_OF_INT = 7
    ARRAY_OF_STRING = 8
    ARRAY_OF_BOOL = 9
    ARRAY_OF_ARRAY = 10


class Array:
    def __init__(self, name, dtype, value=None):
        self.name: str = name
        self.element_type: Type = dtype
        self.value: list[int | str | bool | list] | None = value
        self.is_initialized: bool = False


class Variable:
    def __init__(self, name, dtype, value=None):
        self.name: str = name
        self.type: Type = dtype
        self.value: int | str | bool | Array | None = value
        self.is_initialized: bool = False
