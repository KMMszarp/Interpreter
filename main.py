import sys

from antlr4 import *

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser


def handle_expression(expr):
    for child in expr.getChildren():
        print(type(child), child.getText())


def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")
    lexer = kmmszarpLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = kmmszarpParser(stream)
    tree = parser.program()
    handle_expression(tree)


if __name__ == '__main__':
    main(sys.argv)
