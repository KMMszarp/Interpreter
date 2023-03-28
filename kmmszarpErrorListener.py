from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class kmmszarpErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException("An error occurred while parsing the file. Line: " + str(line) + ", column: " + str(column))
