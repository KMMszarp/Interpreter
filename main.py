import sys

import antlr4

from kmmszarp.kmmszarpLexer import kmmszarpLexer
from kmmszarp.kmmszarpParser import kmmszarpParser


def handle_print(print_expr):
    print(print_expr.getText())


def handle_function_call(call):
    children = [*call.getChildren()]

    if not isinstance(children[0], antlr4.tree.Tree.TerminalNodeImpl):
        raise SyntaxError("Expected function call to start with a keyword")

    # Chyba niepotrzebne
    # assert children[0].getText() == "wywołaj"
    # assert isinstance(children[1], antlr4.tree.Tree.TerminalNodeImpl)

    function_name = children[1].getText()
    if function_name == "napisz":
        handle_print(children[2])
    else:
        raise NotImplementedError("Not able to handle function " + function_name)


def handle_statement(stmt):
    for child in stmt.getChildren():
        if isinstance(child, kmmszarpParser.FunctionCallContext):
            handle_function_call(child)
        else:
            raise NotImplementedError("Not able to handle " + str(type(child)) + " yet")


def handle_expression(expr):
    for child in expr.getChildren():
        if isinstance(child, kmmszarpParser.StatementContext):
            handle_statement(child)
        elif isinstance(child, antlr4.tree.Tree.TerminalNodeImpl):
            pass
        else:
            raise NotImplementedError("Not able to handle " + str(type(child)) + " yet")


def main(argv):
    input_stream = antlr4.FileStream(argv[1], encoding="utf-8")
    lexer = kmmszarpLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = kmmszarpParser(stream)
    tree = parser.program()
    handle_expression(tree)


if __name__ == '__main__':
    main(sys.argv)
