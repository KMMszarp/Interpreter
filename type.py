from enum import Enum
from dataclasses import dataclass
from err import VariableRedeclarationError, VariableNotDeclaredError, VariableNotInitializedError, \
    VariableTypeMismatchError


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

        return self.name


@dataclass
class Array:
    name: str
    element_type: Type
    value: list[int | str | bool | list] | None
    is_initialized: bool = False


class VariableLike:
    """
    Represents a variable or a value of an expression computed during runtime
    """
    dtype: Type
    value: any

    def __init__(self, dtype: Type, value: any):
        self.dtype = dtype
        self.value = value

    def __str__(self):
        if self.dtype == Type.BOOL:
            return "prawda" if self.value else "kłamstwo"

        if self.dtype == Type.INT and self.value < 0:
            return f"minus {abs(self.value)}"

        return str(self.value)


class ParsedExpression(VariableLike):
    """
    Represents a value of an expression computed during runtime
    """
    pass


class Variable(VariableLike):
    """
    Represents a variable
    """
    name: str
    is_initialized: bool

    def __init__(self, name: str, dtype: Type, value: any = None, is_initialized: bool = False):
        super().__init__(dtype, value)
        self.name = name
        self.is_initialized = is_initialized

    def __get__(self, instance, owner):
        if not self.is_initialized:
            raise VariableNotInitializedError(self.name)

        return self

    def set_value(self, value: int | str | bool) -> "Variable":
        self.value = value
        return self

    def get_value(self) -> int | str | bool:
        if not self.is_initialized:
            raise VariableNotInitializedError(self.name)

        return self.value

    def get_dtype(self):
        return self.dtype


class Data:
    def __init__(self):
        self.variables: dict[str, Variable] = {}

    def create_variable(self, name: str, dtype: Type) -> Variable:
        """
        Creates a new uninitialized variable, adds it to data and returns it

        :param name: Name of the variable, must be unique
        :param dtype: Type of the variable
        :returns: Created variable
        :raises VariableRedeclarationError: If variable with given name already exists
        """
        if name in self.variables:
            raise VariableRedeclarationError(name)

        v = Variable(name, dtype)
        self.variables[name] = v

        return self.variables[name]

    def create_and_initialize_variable(self, name: str, dtype: Type, value: str | int | bool | VariableLike) \
            -> Variable:
        """
        Creates and initializes a new variable, same as calling create_variable and set_variable

        :param name: Name of the variable, must be unique
        :param dtype: Type of the variable
        :param value: Value to set the variable to
        :returns: Created variable
        :raises VariableRedeclarationError: If variable with given name already exists
        :raises VariableNotInitializedError: If value is a Variable and it's not initialized
        :raises NotImplementedError: If value is not a Variable, int, str or bool
        """
        self.create_variable(name, dtype)
        self.set_variable(name, value)

        return self.variables[name]

    def get_variable(self, name: str) -> Variable:
        """
        Gets a variable from data

        :param name: Name of the variable to get
        :returns: Variable with given name
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        :raises VariableNotInitializedError: If variable with given name exists but is not initialized
        """
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        if not self.variables[name].is_initialized:
            raise VariableNotInitializedError(name)

        return self.variables[name]

    def set_variable(self, name: str, value: str | int | bool | VariableLike) -> Variable:
        """
        Sets a variable to a given value

        :param name: Name of the variable to set
        :param value: Value to set the variable to
        :returns: Variable with a new value
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        :raises VariableNotInitializedError: If value is a Variable, and it's not initialized
        :raises VariableTypeMismatchError: If value is a VariableLike, and the types mismatch
        :raises NotImplementedError: If value is not a Variable, int, str or bool
        """
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        if isinstance(value, VariableLike):
            if isinstance(value, Variable) and not value.is_initialized:
                raise VariableNotInitializedError(value.name)

            self.variables[name].value = value.value

            if value.dtype != self.variables[name].get_dtype():
                raise VariableTypeMismatchError(name, self.variables[name].get_dtype(), value.dtype)

        elif isinstance(value, (int, str, bool)):
            self.variables[name].value = value

        else:
            raise NotImplementedError(f"Nieznany typ {type(value)}")

        self.variables[name].is_initialized = True
        return self.variables[name]

    def check_if_declared(self, name: str) -> bool:
        """
        Checks if a variable with given name is declared

        :param name: Name of the variable to check
        :return: True if variable is declared, False otherwise
        """
        return name in self.variables

    def remove_variable(self, name: str) -> None:
        """
        Removes a variable from data

        :param name: Name of the variable to remove
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        """
        if name not in self.variables:
            raise VariableNotDeclaredError(name)

        del self.variables[name]
