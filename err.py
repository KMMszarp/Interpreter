from sys import stderr

from antlr4.error.ErrorListener import ErrorListener as BaseListener


class ErrorListener(BaseListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        s = f"Błąd w linii {line}, kolumnie {column} - nie spodziewałem się: {repr(offending_symbol.text)}"
        print(s, file=stderr)


class VariableError(Exception):
    pass


class VariableRedeclarationError(VariableError):
    def __init__(self, variable_name):
        self.variable_name = variable_name


class VariableNotDeclaredError(VariableError):
    def __init__(self, variable_name):
        self.variable_name = variable_name


class VariableNotInitializedError(VariableError):
    def __init__(self, variable_name):
        self.variable_name = variable_name


class ExecutionError(Exception):
    def __init__(self, line, column, msg):
        self.line = line
        self.column = column
        self.msg = msg

    def __str__(self):
        return f"Błąd w linii {self.line}, kolumnie {self.column} - {self.msg}"
