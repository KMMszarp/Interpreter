from sys import stderr

from antlr4.error.ErrorListener import ErrorListener as BaseListener


class ErrorListener(BaseListener):
    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        s = f"Błąd w linii {line}, kolumnie {column} - nie spodziewałem się: {repr(offending_symbol.text)}"
        print(s, file=stderr)
