import sys

import antlr4
from antlr4.error.Errors import ParseCancellationException

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser
from visitor import Visitor
from kmmszarpErrorListener import kmmszarpErrorListener


def main(argv):
    try:
        # Input
        input_stream = antlr4.FileStream(argv[1], encoding="utf-8")
    except Exception as e:
        print("An error occurred while opening the file")

    try:
        # Lexer
        lexer = kmmszarpLexer(input_stream)

        # Parser
        stream = antlr4.CommonTokenStream(lexer)
        parser = kmmszarpParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(kmmszarpErrorListener())
        tree = parser.program()
    except ParseCancellationException as e:
        print(e)
        return

    # Visitor
    visitor = Visitor()
    visitor.visitProgram(tree)


if __name__ == '__main__':
    main(sys.argv)