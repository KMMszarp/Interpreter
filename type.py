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


class Function:
    """
    Represents a function
    """
    name: str
    return_type: Type
    parameters: list[Variable]
    body: list
    return_statement: any

    def __init__(self, name: str, return_type: Type,
                 body: list,
                 parameters: list[Variable] = None,
                 return_statement: any = None):
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.body = body
        self.return_statement = return_statement

    def __get__(self, instance, owner):
        return self

    def get_body(self):
        return self.body

    def get_return_statement(self):
        return self.return_statement

    def get_parameters(self):
        return self.parameters

    def get_return_type(self):
        return self.return_type


class Data:
    def __init__(self):
        self.nest_level: int = 0
        self.variables: dict[int, dict[str, Variable | Function]] = {}

    def create_variable(self, name: str, dtype: Type, nest_level: int = 0) -> Variable:
        """
        Creates a new uninitialized variable, adds it to data and returns it

        :param name: Name of the variable, must be unique
        :param dtype: Type of the variable
        :param nest_level: Nest level of the variable
        :returns: Created variable
        :raises VariableRedeclarationError: If variable with given name already exists
        """

        if nest_level not in self.variables:
            self.variables[nest_level] = {}

        if self.check_if_declared(name):
            raise VariableRedeclarationError(name)

        v = Variable(name, dtype)
        self.variables[nest_level][name] = v

        return self.variables[nest_level][name]

    def create_and_initialize_variable(self, name: str, dtype: Type, value: str | int | bool | VariableLike,
                                       nest_level: int = 0) \
            -> Variable:
        """
        Creates and initializes a new variable, same as calling create_variable and set_variable

        :param name: Name of the variable, must be unique
        :param dtype: Type of the variable
        :param value: Value to set the variable to
        :param nest_level: Nest level of the variable
        :returns: Created variable
        :raises VariableRedeclarationError: If variable with given name already exists
        :raises VariableNotInitializedError: If value is a Variable, and it's not initialized
        :raises NotImplementedError: If value is not a Variable, int, str or bool
        """
        self.create_variable(name, dtype, nest_level)
        self.set_variable(name, value, nest_level)

        return self.variables[nest_level][name]

    def get_variable(self, name: str, nest_level: int = 0) -> Variable:
        """
        Gets a variable from data

        :param name: Name of the variable to get
        :param nest_level: Nest level of the variable
        :returns: Variable with given name
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        :raises VariableNotInitializedError: If variable with given name exists but is not initialized
        """

        if not self.check_if_available(name, nest_level):
            raise VariableNotDeclaredError(name)

        if not self.variables[nest_level][name].is_initialized:
            raise VariableNotInitializedError(name)

        return self.variables[nest_level][name]

    def set_variable(self, name: str, value: str | int | bool | VariableLike, nest_level: int = 0) -> Variable:
        """
        Sets a variable to a given value

        :param name: Name of the variable to set
        :param value: Value to set the variable to
        :param nest_level: Nest level of the variable
        :returns: Variable with a new value
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        :raises VariableNotInitializedError: If value is a Variable, and it's not initialized
        :raises VariableTypeMismatchError: If value is a VariableLike, and the types mismatch
        :raises NotImplementedError: If value is not a Variable, int, str or bool
        """

        if not self.check_if_available(name, nest_level):
            raise VariableNotDeclaredError(name)

        if isinstance(value, VariableLike):
            if isinstance(value, Variable) and not value.is_initialized:
                raise VariableNotInitializedError(value.name)

            self.variables[nest_level][name].value = value.value

            if value.dtype != self.variables[nest_level][name].get_dtype():
                raise VariableTypeMismatchError(name, self.variables[nest_level][name].get_dtype(), value.dtype)

        elif isinstance(value, (int, str, bool)):
            self.variables[nest_level][name].value = value

        else:
            raise NotImplementedError(f"Nieznany typ {type(value)}")

        self.variables[nest_level][name].is_initialized = True
        return self.variables[nest_level][name]

    def check_if_declared(self, name: str) -> bool:
        """
        Checks if a variable with given name is declared

        :param name: Name of the variable to check
        :return: True if variable is declared, False otherwise
        """
        # TODO: Czy można przykrywać zmienne o tej samej nazwie w różnych zakresach?
        # TODO: można zdeklarować w wyższym jeśli jest tylko w niższym
        for i in range(0, len(self.variables)):
            if name in self.variables[i]:
                return True

        return False

    def check_if_available(self, name: str, nest_level: int = 0) -> bool:
        """
        Checks if a variable with given name is available

        :param name: Name of the variable to check
        :param nest_level: Nest level of the variable
        :return: True if variable is available, False otherwise
        """
        if not self.check_if_declared(name):
            return False

        for i in range(0, nest_level + 1):
            if name in self.variables[i]:
                return True

        return False

    def remove_variable(self, name: str, nest_level: int = 0) -> None:
        """
        Removes a variable from data

        :param name: Name of the variable to remove
        :param nest_level: Nest level of the variable
        :raises VariableNotDeclaredError: If variable with given name doesn't exist
        """

        if not self.check_if_available(name, nest_level):
            raise VariableNotDeclaredError(name)

        del self.variables[nest_level][name]

    def declare_function(self, name: str, return_type: Type,
                         body: list,
                         parameters: list[Variable] = [],
                         return_statement: any = None, nest_level: int = 0) -> Function:
        """
        Declares a function
        :param name: Name of the function to declare
        :param return_type: Type of the function's return value
        :param body: Tree of the function's body
        :param parameters: Parameters of the function
        :param return_statement: Return statement of the function
        :param nest_level: Nest level of the function
        :return: Returns the declared function
        """
        prefixed_name = f"$_{name}"  # Create variable that is impossible to declare in code
        if self.check_if_declared(prefixed_name):
            raise VariableRedeclarationError(name)

        if nest_level not in self.variables:
            self.variables[nest_level] = {}

        f = Function(name, return_type, body, parameters, return_statement)

        self.variables[nest_level][prefixed_name] = f

        return self.variables[nest_level][prefixed_name]

    def get_function(self, name: str, nest_level: int = 0) -> Function:
        """
        Gets a function with given name
        :param name: Name of the function to get
        :param nest_level: Nest level of the function
        :return: Returns the function
        """
        prefixed_name = f"$_{name}"
        if not self.check_if_function_available(name, nest_level):
            raise VariableNotDeclaredError(name)

        return self.variables[nest_level][prefixed_name]

    def remove_function(self, name: str, nest_level: int = 0) -> None:
        """
        :param name: Name of the function to remove
        :param nest_level: Nest level of the function
        """
        prefixed_name = f"$_{name}"
        self.remove_variable(prefixed_name, nest_level)

    def check_if_function_declared(self, name: str) -> bool:
        """
        :param name: Name of the function to check
        :return: True if function is declared, False otherwise
        """
        prefixed_name = f"$_{name}"
        return self.check_if_declared(prefixed_name)

    def check_if_function_available(self, name: str, nest_level: int = 0) -> bool:
        """
        :param name: Name of the function to check
        :param nest_level: Nest level of the function
        :return: True if function is available, False otherwise
        """
        prefixed_name = f"$_{name}"
        return self.check_if_available(prefixed_name, nest_level)

    def increase_nest(self) -> int:
        """
        Increases the nest level
        :return: New nest level
        """
        self.nest_level += 1
        return self.nest_level

    def decrease_nest(self) -> int:
        """
        Decreases the nest level
        :return: New nest level
        """
        self.nest_level -= 1
        return self.nest_level

    def get_nest_level(self) -> int:
        """
        Gets the current nest level
        :return: Current nest level
        """
        return self.nest_level

    def get_variables(self, nest_level: int = 0) -> dict[str, Variable]:
        """
        Gets variables from given nest level
        :param nest_level: Nest level of the variables
        :return: Variables from given nest level
        """
        if nest_level not in self.variables:
            self.variables[nest_level] = {}
        return self.variables[nest_level]

    def set_variables(self, variables: dict[str, Variable], nest_level: int = 0):
        """
        Sets variables in given nest level
        :param variables: Variables to set
        :param nest_level: Nest level of the variables
        :return:
        """
        self.variables[nest_level] = variables
