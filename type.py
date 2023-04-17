from enum import Enum
from dataclasses import dataclass
from err import ExecutionError, VariableRedeclarationError, VariableNotDeclaredError, VariableNotInitializedError

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

    @staticmethod
    def from_string(s: str) -> "Type":
        if s == "liczba":
            return Type.INT
        elif s == "napis":
            return Type.STRING
        elif s == "prawdziwość":
            return Type.BOOL
        elif s == "nicość":
            return Type.VOID

        raise NotImplementedError(f"Nieznany typ {s}")

    def __str__(self):
        if self == Type.INT:
            return "liczba"
        elif self == Type.STRING:
            return "napis"
        elif self == Type.BOOL:
            return "prawdziwość"
        elif self == Type.VOID:
            return "nicość"

        return self.__class__.__name__


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
        if name in self.variables:
            raise VariableRedeclarationError(name)

        v = Variable(name, dtype, None)
        self.variables[name] = v

    def create_and_initialize_variable(self, name: str, dtype: Type, value: any) -> any:
        self.create_variable(name, dtype)
        self.set_variable(name, value)

        return value

    def get_variable(self, name: str) -> any:
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        if not self.variables[name].is_initialized:
            raise VariableNotInitializedError(name)

        return self.variables[name]

    def set_variable(self, name: str, value: any):
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        if isinstance(value, Variable):
            self.variables[name].value = value.value
            self.variables[name].is_initialized = True

            return value

        self.variables[name] = value
        self.variables[name].is_initialized = True

        return self.variables[name]

    def check_if_declared(self, name: str) -> bool:
        return name in self.variables

    def remove_variable(self, name: str):
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        del self.variables[name]