from enum import Enum
from dataclasses import dataclass


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


@dataclass
class Array:
    name: str
    element_type: Type
    value: list[int | str | bool | list] | None
    is_initialized: bool = False


@dataclass
class Variable:
    name: str
    dtype: Type
    value: any = None
    is_initialized: bool = False

    def __str__(self):
        if self.dtype == Type.BOOL:
            return "prawda" if self.value else "kłamstwo"

        return str(self.value)


class Data:
    def __init__(self):
        self.variables = {}

    def create_variable(self, name: str, dtype: Type):
        v = Variable(name, dtype, None)
        self.variables[name] = v

    def initialize_variable(self, name: str, value: any) -> None:
        if name not in self.variables:
            raise Exception(f"Variable {name} not found")

        self.variables[name].value = value
        self.variables[name].is_initialized = True

    def create_and_initialize_variable(self, name: str, dtype: Type, value: any) -> any:
        self.create_variable(name, dtype)
        self.initialize_variable(name, value)

        return value

    def get_variable(self, name: str) -> any:
        if name not in self.variables:
            raise Exception(f"Variable {name} not found")
        return self.variables[name]

    def set_variable(self, name: str, value: any):
        if name not in self.variables:
            raise Exception(f"Variable {name} not found")
        self.variables[name] = value

        return value