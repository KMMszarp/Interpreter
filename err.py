from kmmszarpErrorListener import kmmszarpErrorListener as baseListener


class kmmszarpErrorListener(baseListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Błąd w linii {line}, kolumnie {column} - nie spodziewałem się: {repr(offendingSymbol.text)}")