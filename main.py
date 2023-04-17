import sys

import antlr4

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser

from visitor import Visitor
from err import ErrorListener, ExecutionError


def main(argv):
    # Input
    try:
        input_stream = antlr4.FileStream(argv[1], encoding="utf-8")
    except FileNotFoundError:
        print("Plik nie istnieje")
        sys.exit(1)
    except KeyError:
        print("Nie podano pliku")
        sys.exit(1)
    except Exception as e:
        print("Nie udało się otworzyć pliku: " + e)
        sys.exit(1)

    # Lexer
    lexer = kmmszarpLexer(input_stream)
    lexer.removeErrorListeners()

    # Parser
    stream = antlr4.CommonTokenStream(lexer)
    parser = kmmszarpParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorListener())
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        sys.exit(2)

    # Visitor
    visitor = Visitor()

    try:
        visitor.visitProgram(tree)
    except ExecutionError as e:
        print(e)
        sys.exit(3)


if __name__ == '__main__':
    main(sys.argv)
