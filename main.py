import sys

import antlr4

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser
from visitor import Visitor


def main(argv):
    # Input
    input_stream = antlr4.FileStream(argv[1], encoding="utf-8")

    # Lexer
    lexer = kmmszarpLexer(input_stream)

    # Parser
    stream = antlr4.CommonTokenStream(lexer)
    parser = kmmszarpParser(stream)
    tree = parser.program()

    # Visitor
    visitor = Visitor()
    visitor.visitProgram(tree)


if __name__ == '__main__':
    main(sys.argv)
